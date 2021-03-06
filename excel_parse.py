import excel_process  as EP
import logger as log

class  Reg_Class_Test():
    reg_filed_num = 0
    field_name_list = []
    def __init__(self,pos_row,pos_col,Bit,cell_merge_flag,cell_merge_bit_list):
        self.cell_pos_row = pos_row   #cell的起始位置
        self.cell_pos_col = pos_col
        self.cell_merge_flag = cell_merge_flag   #cell 是否Merge
        self.cell_merge_col_num = 0   #cell merge 的行列数
        self.cell_merge_row_num = 0
        self.cell_merge_bit_list= cell_merge_bit_list
        self.cell_parse_result_list = []
        self.Bit =Bit
    @classmethod  # 定义类方法,类方法的第一个参数是cls
    def add_attr(cls,attr_name,value):
        setattr(cls,attr_name,value)




'''
filed_bit_vastart_bit,end_bit 进行filedyu进行field的解析
'''
def filed_bit_value(bit_start_in_all_bit, end_bit,data_list):
    bit_length = end_bit - bit_start_in_all_bit + 1
    int_index = bit_start_in_all_bit // 32  # 以int为单位，在第几个int中
    bit_start_in_int = bit_start_in_all_bit % 32 #以bit为单位，在int中的哪个bit开始

    '''
    # 当是字符串时，使用int(a,16), 否则使用Int（）
    # result = ((int(data_list[int_index], 16) >> (bit_start_in_int)) & ((1 << bit_length) - 1))
    '''
    #开始解析
    if (bit_start_in_int + bit_length > 32):   # cross the int
        cross_int_flag = 1
        first_int_bit_length = 32 - bit_start_in_int #第一个int中的有效bit位
        second_int_bit_length = bit_length + bit_start_in_int  - 32  #第二个int中残留的bit位
        temp_data_1 = ((int(data_list[int_index])  >> (bit_start_in_int)) & ((1 << first_int_bit_length) -1) )
        #第二个int 从0开始取second_int_bit_length 这么长bit
        temp_data_2 =  ((int(data_list[int_index + 1])  >> (0)) & ((1 << second_int_bit_length) -1) )
        result = (temp_data_2 << first_int_bit_length) | temp_data_1
    else:
        cross_int_flag = 0
        first_int_bit_length = bit_start_in_int + 1
        # 先右移，再&上响应的bit位
        #当是字符串时，使用int(a,16), 否则使用Int（）
        # result = ((int(data_list[int_index], 16) >> (bit_start_in_int)) & ((1 << bit_length) - 1))
        result = ((int(data_list[int_index])  >> (bit_start_in_int)) & ((1 << bit_length) -1) )
    return  (result)




'''
根据reg_class 中的bit位段 进行数据的解析,
reg_class: reg 的class定义
data_list: 数据形成的List，每个list是以32bit 组成的元素list 
loop_flag:是否循环解析
loop_times: 在loop_flag= Ture时有效，
'''
def single_reg_parse(reg_class,data_list,data_format):
    single_time_parse_result = []
    try:
        for cell_bit in reg_class.cell_merge_bit_list:
            #log.logger.debug(cell_bit)
            #得到每个bit段的start_bit_addr , end_bit_addr
            bit = cell_bit.lstrip("[")
            bit_list = bit.rstrip("]").split(":")
            if (len(bit_list) == 1):
                start_field = end_field = int(bit_list[0])
            else:
                end_field = int(bit_list[0])
                start_field = int(bit_list[1])
            log.logger.debug("start = {},end = {}".format(start_field,end_field))
            result = filed_bit_value(start_field,end_field,data_list)
            if (data_format == 16):
                single_time_parse_result.append(hex(result))
            else:
                single_time_parse_result.append(result)
                
            log.logger.debug("cell_bit = {},result = {}".format(cell_bit,result))

        # 将单次parse的结果存放在reg_class中
        reg_class.cell_parse_result_list.append(single_time_parse_result)


    except Exception as err:
        log.logger.error(err)
        log.logger.error("reg parse exception occured")

    return reg_class


'''
#根据excel_dict中的key，取得excel_dict中的REG_CLASS,然后去data_dict中找到对应地址的数据，然后进行解析。
使用int(地址)
#要设置寄存器个数,当读取的reg个数大于要解析的寄存器个数时，要根据寄存器个数来判断，否则当只需要解析部分reg，
并且重复解析时，会出现重复部分的寄存器地址和剩余的寄存器地址相等的情况，
例如:对reg0 进行重复4次解析，其地址为0,4,,8,12,但是剩余的寄存器地址也有4,8,12,所以会多解析，浪费时间。
parse_reg_num: 要解析的reg个数
loop_time: 解析的循环次数
loop_range:解析一轮的地址范围
'''
def excel_parse_process(excel_dict, data_dict,parse_reg_num, loop_time,loop_range,data_format,statusbar):
    parse_reg_index = 0
    # 循环loop_time 的次数
    for key in excel_dict.keys():
        reg = excel_dict[key]
        reg.cell_parse_result_list.clear()  # 每次启动之前，清除之前的解析结果
        try:
            #使用16进制进行str 的转化
            if (type(int(key,16)) is int): #key是数字，表明地址
                parse_reg_index = parse_reg_index + 1 #记录已经解析的寄存器个数
                reg_addr = int(key, 16)

                if (parse_reg_index <= parse_reg_num):
                    for loop in range(loop_time):
                        data_addr = reg_addr + (loop * loop_range)
                        #去data_dict中找到对应地址的数据
                        data_list = data_dict.get(data_addr,4294967295)
                        log.logger.info("\n--------------------------------------------------------------")
                        log.logger.info("reg index = {0},reg_addr = {1},loop_index = {2},data_addr = {3},data = {4}".format(
                            parse_reg_index,hex(reg_addr),loop,hex(data_addr),(data_list)))
                        #根据reg中的数据bit位去解析bit位
                        temp_class = single_reg_parse(reg,data_list,data_format)
                        excel_dict[key] = temp_class
                        statusbar.PushStatusText("parse reg:{0},loop:{1}".format(reg_addr,loop + 1),field = 2)
                else:
                    pass
        except  Exception as err:
            log.logger.error(err)
            #有可能excel_dict中的key 不是int地址
            log.logger.error("excel dict exception occured")


'''
 将解析之后的数据写出到excel_文件中去
'''
def excel_parse_output(excel_dict, excel_path,statusbar):
    output_excel = EP.excel_item(excel_path)
    output_excel.excel_open()
    output_excel.open_sheet(0)

    for key in excel_dict.keys():
        try:
            if (type(int(key, 16)) is int):  # key是数字，表明地址
                reg = excel_dict[key]
                start_row = reg.cell_pos_row
                start_col = reg.cell_pos_col

                output_excel.write_range(output_excel.sheet,
                                         start_row,
                                         # 在所有列之后再加3列之后输出
                                         start_col + reg.reg_filed_num + 3 ,
                                         True,
                                         reg.cell_parse_result_list)
                statusbar.PushStatusText("output reg:{0}".format(key), field=3)
                '''
                 #将多次循环的解析结果依次写入不同的列中
                for parse_list_index in range(len(reg.cell_parse_result_list)):
                    data_list = reg.cell_parse_result_list[parse_list_index]
                    output_excel.write_range(output_excel.sheet,
                                 start_row ,
                                 # 在所有列之后再加3列之后输出
                                 start_col + reg.reg_filed_num + 3 + parse_list_index,
                                 True,
                                 data_list)
                    statusbar.PushStatusText("output reg:{0}".format(key), field=3)
              '''

        except:
            pass
    output_excel.save(output_excel.wb)
    output_excel.close(output_excel.wb)



'''
  测试代码

'''

'''
if __name__ == "__main__":
    excel_dict = {}
    data_dict = {}
    cell_merge_bit_list = ["[95:32]","[31:28]","[27:16]","[15:0]"]
    reg1 = Reg_Class_Test(1,1,32,True,cell_merge_bit_list)

    cell_merge_bit_list = ["[31]", "[30:12]", "[11:6]", "[5:0]"]
    reg2 = Reg_Class_Test(33, 2, 32, True, cell_merge_bit_list)

    excel_dict["0x0000"] = reg1
    #excel_dict["below "] = reg2
    #excel_dict["0x4"] = reg2

    data_dict[0]= [0xffffffd4,0xffffffd5,0xffffffd6]  #
    data_dict[12] =[0xffffffd7,0xffffffd8,0xffffffd9]
    #data_dict[1] = ["0xfffffd5"]
    excel_parse_process(excel_dict,data_dict,2,12)
    excel_parse_output(excel_dict,r"./dp_cc_parse_result_hhh.xlsx")
    pass
'''
