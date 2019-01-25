import struct
class  Reg_Class():
    reg_filed_num = 0
    field_name_list = []
    def __init__(self,pos_row,pos_col):
        self.cell_pos_row = pos_row   #cell的起始位置
        self.cell_pos_col = pos_col
        self.cell_merge_flag = 0   #cell 是否Merge
        self.cell_merge_col_num = 0   #cell merge 的行列数
        self.cell_merge_row_num = 0
        self.cell_merge_bit_list= []  #寄存器中包含的各个位段的bit 起始位置和结束位置
        self.cell_parse_result_list = [] #寄存器中包含的各个位段的解析结果存放队列
    @classmethod  # 定义类方法,类方法的第一个参数是cls
    def add_attr(cls,attr_name,value):
        setattr(cls,attr_name,value)






class  Binary_File(object):
    def __init__(self,path):
        self.filesize = 0
        self.segment_length = 0
        self.loop_parse_flag = False
        self.path = path


    '''  
    根据reg的bit长度，以及要读取的reg的个数，是否循环读取，以及大小端模式进行数据的读取 
    reg的bit长度最小是32bit,最长是256bit,每次读取32bit,读取之后进行大小端解析，
    并且根据总的bit长度，和大小端模式，确定是否需要地址倒序
    '''
    def Binary_file_read_and_unpack(self,unit_bit, unit_number,loop_flag, loop_number,ending_mode):

        if (ending_mode == 1): #小端模式
            ending_mode_str = "<"
        elif (ending_mode == 2):  #大端模式
            ending_mode_str = ">"
        else: #默认使用小端模式
            ending_mode_str = "<"

        #确认要读取的字节长度
        if loop_flag == True:
            read_num = int(unit_number) * int(loop_number)
        else:
            read_num= int(unit_number)
        parse_byte = int(unit_bit) // 8 #byte 个数
        unpack_int_number = str(parse_byte // 4)
        unpack_pattern = ending_mode_str + unpack_int_number + "I"
        print("unpack pattern = %s" %unpack_pattern)
        data_dict = {}
        with open(self.path,"rb") as f_p:
            for read_idx in range(read_num):
                unpack_result = ()
                unpack_list = []
                temp_data_addr = f_p.tell() #得到数据的起始位置
                temp_data = f_p.read(parse_byte)

                unpack_result = struct.unpack(unpack_pattern,temp_data) #返回值是tuple
                for item in unpack_result:
                    unpack_list.append(item)

                ''' 不需要反序，因为寄存器中的地址是从0开始的，从小到大的。
                if ending_mo== ">" :
                    pass
                else: #小端模式时，地址和数据需要倒序
                    unpack_list.reverse()  # 进行存储区域数据顺序倒置
              '''
                data_dict[temp_data_addr] = unpack_list
                #测试代码
                print(([ hex(x) for x in data_dict[temp_data_addr]]))


        return  data_dict




'''
if __name__ == "__main__":
    b_file = Binary_File(r"D:\git_clone\small_tools_develop\binary_excel_parse_git\binary_excel_parse\test_asic_reg.bin")
    data_dict = b_file.Binary_file_read_and_unpack(256,2,True,4,"<")
    pass
'''



