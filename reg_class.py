class  Reg_Class():
    reg_filed_num = 0
    field_name_list = []
    def __init__(self,pos_row,pos_col):
        self.cell_pos_row = pos_row   #cell的起始位置
        self.cell_pos_col = pos_col
        self.cell_merge_flag = 0   #cell 是否Merge
        self.cell_merge_col_num = 0   #cell merge 的行列数
        self.cell_merge_row_num = 0
        self.cell_merge_bit_list= []
    @classmethod  # 定义类方法,类方法的第一个参数是cls
    def add_attr(cls,attr_name,value):
        setattr(cls,attr_name,value)






class  Binary_File(object):
    def __init__(self,path):
        self.filesize = 0
        self.segment_length = 0
        self.loop_parse_flag = False
        self.path = path

    def Binary_file_read(self,unit_bit, unit_number,loop_flag, loop_number):
        #确认要读取的字节长度
        if loop_flag == True:
            read_num = int(unit_number) * int(loop_number)
        else:
            read_num= int(unit_number)
        parse_byte = int(unit_bit) // 8 #byte 个数
        data_dict = {}
        with open(self.path,"rb") as f_p:
            for read_idx in range(read_num):
                temp_data_addr = f_p.tell() #得到数据的起始位置
                temp_data = f_p.read(parse_byte)
                print(temp_data_addr)
                print(temp_data)
                data_dict[temp_data_addr] = temp_data
        return  data_dict



'''
if __name__ == "__main__":
    b_file = Binary_File(r"D:\git_clone\small_tools_develop\binary_excel_parse_git\binary_excel_parse\test_asic_reg.bin")
    data_dict = b_file.Binary_file_read(32,2,True,4)
    pass
'''



