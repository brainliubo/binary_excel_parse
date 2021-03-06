import xlwings as XL
from  reg_class import Reg_Class
import os
import shutil
import time
import logger as log

class excel_item(object):
    def __init__(self,file_path):
        self.column = 0
        self.row = 0
        self.validaddr_number = 0
        self.path = file_path
        self.wb = None
        self.sheet = None
        self.sheet_valid = False
        self.row_offset = 0    #开始读取时的row offset
        self.column_offset = 0 # 开始读取时的column offset
        self.new_excel_flag = 0
    #检查excel的格式是否符合预期
    def excel_open(self):
        app = XL.App(visible=False ,add_book=False)
        if os.path.exists(self.path):
            self.wb = app.books.open(self.path)
            self.new_excel_flag =False
            
        else:
            self.wb = app.books.add() #新建立一个Book，并且保存，然后打开
            self.wb.save(self.path)
            self.wb = app.books.open(self.path) #self.wb = XL.Book(self.path)
            self.new_excel_flag = True
            
        return self.wb.sheets

    def open_sheet(self,sheet_index):
        self.sheet = self.wb.sheets[sheet_index] # EXCEL的sheet可以通过excel指定来解析

    def write_range(self,sheet,start_row,start_col, transpose_flag,data_list):
        sheet.range((start_row,start_col)).options(transpose = transpose_flag).value = data_list


    def save(self,wb):
        wb.save()
    def close(self,wb):
        wb.close()

    '''
    检查excel的某个sheet的格式是否合理,必须包含多个合格的关键字,
    这里可以改进，不输入row_offset, column_offset,顺序读第一列，读到第一个offset，
    获取这一行的所有参数
    '''
    def  format_check(self,sheet,row_offset,column_offset):
        #读取第一个有效行的描述字段，横向读取100列的字段
        try:
            column_list_row = sheet.range((row_offset,column_offset),(row_offset,column_offset + 100)).value

            column_list = []
            for item in column_list_row:
                if (item  !=  None):
                    column_list.append(item.rstrip().lstrip())  #将column_list中的空格去掉

            #根据excel的域动态添加类的属性进行，得到spec_reg_class
            for item in column_list:
                Reg_Class.add_attr(item,0)

            Reg_Class.reg_filed_num = len(column_list)  # 记录总的field
            # 使用extend，将前一个list的元素依次放入，如果用append,则是将List作为一个element 放入队列
            Reg_Class.field_name_list.extend(column_list)
            log.logger.debug("start to parse excel ")
            log.logger.debug(Reg_Class.__dict__)
            log.logger.debug(Reg_Class.field_name_list)

            if (("offset"  not in column_list) or ("RegName"  not in column_list)
                or ("Width"  not in column_list) or ("FieldName"  not in column_list)
                or ("Bit"  not in column_list)):
                self.sheet_valid = False
                log.logger.error("sheet is invalid，the start row's field doesn't satisfy the conditions")
                return ("sheet 无效，起始行不包含全部指定的关键字，请检查起始行的值")

            else:
                self.sheet_valid = True
                self.column_valid_number = column_list.__len__()
                log.logger.info("sheet is valid,pls go on ")
                return ("sheet 格式检查合格，可以继续操作!")

        except Exception as err:
            log.logger.error("the input start row is wrong ,pls check it ")
            return "输入的起始行有误，检查该行是否包含指定的关键字"
            pass

    def sheet_cell_read(self,sheet,row,col):
        cell_item = Reg_Class(row, col)
        merge_row_number = cell_item.cell_merge_row_num
        null_row_number = 0
        # 通过fieldname来判断 是否有merge cell
        merge_judge_col_index = Reg_Class.field_name_list.index("Bit")

        start_time = time.clock()
        # 读取一行的元素，填写class
        '''
        for index in range(Reg_Class.reg_filed_num):
            cell_item.__dict__[Reg_Class.field_name_list[index]] = sheet.range((row, col + index)).value
       '''
        #读第一列：
        cell_item.__dict__[Reg_Class.field_name_list[0]] = sheet.range((row, col)).value
        #读关键字所在的列
        cell_item.__dict__[Reg_Class.field_name_list[merge_judge_col_index]] = sheet.range((row, col + merge_judge_col_index)).value


        end_time = time.clock()
        log.logger.debug("first row time:{} ".format(end_time - start_time))

        start_time = time.clock()
        #判断行合并的情况
        #如果关键字段的所在列的cell中有值，则判断下一行是否为空，
        if(cell_item.__dict__[Reg_Class.field_name_list[merge_judge_col_index]] != None):
            cell_item.cell_isreg_flag = True  # 是一个合格的寄存器
            cell_item.cell_merge_bit_list.append(cell_item.Bit)
            # step1: 判断合并
            # 判断后面行的offset 列和bit 列的值，确认是否是一个merge cell
            #第一列的下一行的值是None，并且关键字的那一列的值不是None,说明是合并的寄存器
            while (sheet.range((row+ merge_row_number + 1, col)).value == None):
                # 列不变，行变
                judge_value = sheet.range(((row + merge_row_number + 1), (col + merge_judge_col_index))).value
                if (None != judge_value):
                    merge_row_number = merge_row_number + 1
                    cell_item.cell_merge_bit_list.append(judge_value)
                else:
                    null_row_number = null_row_number + 1
                    if (null_row_number == 5):       #连续后面10行都是空，那么认为读取excel结束
                        break

            cell_item.cell_merge_row_num = merge_row_number + 1  # 加上第一行

            end_time = time.clock()
            log.logger.debug("judge merge time:{}".format(end_time - start_time))

            # step2: 判断行合并，在当前版本中省略

            #step2: 返回cell_item
            if (cell_item.cell_merge_col_num > 1) or (cell_item.cell_merge_row_num > 1):
                cell_item.cell_merge_flag = True



        else: #空行也要加一行
            cell_item.cell_isreg_flag = False #不是一个合格的寄存器
            cell_item.cell_merge_row_num = merge_row_number + 1  # 加上第一行

        return cell_item

    def sheet_cell_process(self,sheet,start_row,end_row,statusbar):
        #cell_item_list = [ ]
        cell_item_dict = { } #存放在 dict 中
        end_row_flag = False
        row = start_row
        while row < end_row:
            cell_item = self.sheet_cell_read(sheet,row,1)
            row = row + cell_item.cell_merge_row_num  # 更新，

            #只记录合格的reg
            if (cell_item.cell_isreg_flag == True):
                cell_item_dict[cell_item.__dict__[Reg_Class.field_name_list[0]]] = cell_item
            statusbar.PushStatusText("excel read:{}".format(row), field = 0)
   
        # 返回cell_item_dict 
        return  cell_item_dict











'''
excel_item = excel_item(r"dp_cc_reg.xlsx")
#excel_item.sheet_read(0)

excel_item.format_check(excel_item.sheet,1,1)

excel_item.sheet_cell_process(excel_item.sheet)






excel_item.close(excel_item.wb)
'''


