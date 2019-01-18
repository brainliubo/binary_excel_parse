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
    def __init__(self):
        self.filesize = 0
        self.segment_length = 0
        self.loop_parse_flag = False

    def Binary_file_read(self,path):
        with open(path,"rb") as f_p:
            pass




