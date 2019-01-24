
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
        self.cell_pares_result_list = []
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

    if (bit_start_in_int + bit_length > 32):   # cross the int
        cross_int_flag = 1
        first_int_bit_length = 32 - bit_start_in_int #第一个int中的有效bit位
        second_int_bit_length = bit_length + bit_start_in_int  - 32  #第二个int中残留的bit位
        temp_data_1 = ((int(data_list[int_index],16)  >> (bit_start_in_int)) & ((1 << first_int_bit_length) -1) )
        #第二个int 从0开始取second_int_bit_length 这么长bit
        temp_data_2 =  ((int(data_list[int_index + 1],16)  >> (0)) & ((1 << second_int_bit_length) -1) )
        result = (temp_data_2 << first_int_bit_length) | temp_data_1
    else:
        cross_int_flag = 0
        first_int_bit_length = bit_start_in_int + 1
        # 先右移，再&上响应的bit位
        result = ((int(data_list[int_index],16)  >> (bit_start_in_int)) & ((1 << bit_length) -1) )
    return  hex(result)




'''
根据reg_class 中的bit位段 进行数据的解析,
reg_class: reg 的class定义
data_list: 数据形成的List，每个list是以32bit 组成的元素list 
'''
def single_reg_parse(reg_class,data_list):
    try:
        for cell_bit in reg_class.cell_merge_bit_list:
            print(cell_bit)
            #得到每个bit段的start_bit_addr , end_bit_addr
            bit = cell_bit.lstrip("[")
            bit_list = bit.rstrip("]").split(":")
            if (len(bit_list) == 1):
                start_field = end_field = int(bit_list[0])
            else:
                end_field = int(bit_list[0])
                start_field = int(bit_list[1])
            print("start = {},end = {}".format(start_field,end_field))
            result = filed_bit_value(start_field,end_field,data_list)
            reg_class.cell_pares_result_list.append(result)
            print("cell_bit = {},result = {}".format(cell_bit,result))

    except Exception as err:
        print(err)
        print("reg parse exception occured")



'''
#根据excel_dict中的key，取得excel_dict中的REG_CLASS,然后去data_dict中找到对应地址的数据，然后进行解析。
使用int(地址)
'''
def excel_parse(excel_dict, data_dict):
    for key in excel_dict.keys():
        print((key))
        try:
             #使用16进制进行str 的转化
            if (type(int(key,16)) is int): #key是数字，表明地址
                reg_addr = int(key,16)
                #去data_dict中找到对应地址的数据
                data_list = data_dict.get(reg_addr,4294967295)
                reg = excel_dict[key]
                #根据reg中的数据bit位去解析bit位
                single_reg_parse(reg,data_list)
        except  Exception as err:
            print(err)
            #有可能excel_dict中的key 不是int地址
            print("excel dict exception occured")





if __name__ == "__main__":
    excel_dict = {}
    data_dict = {}
    cell_merge_bit_list = ["[95:64]","[63:50]","[49:28]","[27:16]","[15:0]"]
    reg1 = Reg_Class_Test(1,2,32,True,cell_merge_bit_list)

    cell_merge_bit_list = ["[31]", "[30:12]", "[11:6]", "[5:0]"]
    reg2 = Reg_Class_Test(1, 2, 32, True, cell_merge_bit_list)

    excel_dict["0x0000"] = reg1
    #excel_dict["below "] = reg2
    #excel_dict["0x4"] = reg2

    data_dict[0]= ["0xffffffd4","0xfedc2054","0xabcdef12"]  #
    #data_dict[1] = ["0xfffffd5"]
    excel_parse(excel_dict,data_dict)



