import wx
import UI
import xlwings
import excel_process  as EP
import os
from  reg_class import Binary_File
from  excel_parse import excel_parse_process
from excel_parse import excel_parse_output
import shutil



global excel_file
global data_dict
global excel_dict
global loop_time
global loop_range
global parse_data_format
global output_path

excel_dict = {}
data_dict = {}
parse_data_format = 16 #默认16进制
loop_time = 1 # 默认循环1次


class myframe(UI.MyFrame):
    def output_excel_changed( self, event ):
	    global output_path
	    # 设置输出文件地址，如果文件不存在，则负责原始
	    output_path = self.output_excel_filePicker.GetPath()
	    src_path = self.excel_filePicker.GetPath()
	    # 不存在此文件，则复制源excel文件到目的地址，并重命名
	    if (os.path.exists(output_path) == False):
		    shutil.copy(src_path, output_path)
      
		    
    def loop_parse_check( self, event ):
        if self.loop_checkBox.IsChecked() == True:
            self.loop_textctrl.Enable()
        else:
            self.loop_textctrl.Clear()
            self.loop_textctrl.Disable()

    def output_choice_select( self, event ):
        if self.output_choice.GetSelection() == 0:
            #输出excel
            self.output_excel_filePicker.Enable()
            self.output_log_filePicker.Disable()
        else:
            #输出文本文件
            self.output_log_filePicker.Enable()
            self.output_excel_filePicker.Disable()
    '''
    文件选择时的处理,打开excel，并读取sheet的name,填入sheet_choice
    '''
    def excel_file_select(self,event):
        global excel_file

        # disable button ,clear the textctrl's content
        self.excel_check_button.Disable()
        self.startrow_textCtrl.Clear()
        self.endrow_textCtrl.Clear()

        # 设置choice的sheet
        excel_file = EP.excel_item(self.excel_filePicker.GetPath())
        sheet_list = excel_file.excel_open()
        i = 0
        for item in sheet_list:
            print(item.name)
            self.sheet_choice.SetString(i,str(item.name))
            i = i+1
        print(type(sheet_list))


    def  binary_file_select( self, event ):
        self.binary_file_size_textctrl.Value = str(os.path.getsize( self.binary_filePicker.GetPath()))
        #disable button ,clear the textctrl's content
        self.parse_check_button.Disable()
        self.parse_unit_choice.SetString(0,"")
        self.parse_number_textCtrl.Clear()
        self.loop_textctrl.Clear()
        self.max_loop_textCtrl.Clear()
        self.loop_textctrl.Disable()

 


    '''
    excel check button的使能和去使能
    '''
    def excel_check_button_process( self, event ):
        index = self.sheet_choice.GetSelection()
        if ((self.sheet_choice.GetString(index) != "") and (self.startrow_textCtrl.GetValue() != "")
             and (self.endrow_textCtrl.GetValue()!= "")):
            self.excel_check_button.Enable()
        else:
            self.excel_check_button.Disable()

    '''
    binary button 的使能和去使能
    '''
    def binary_check_button_process( self, event ):
        index = self.parse_unit_choice.GetSelection()
        if ((self.parse_unit_choice.GetString(index)!= "") and (self.parse_number_textCtrl.GetValue() != "")
             and (self.ending_choice.GetCurrentSelection() != 0)):
            self.parse_check_button.Enable()
            temp_value = int(self.binary_file_size_textctrl.GetValue()) // (int(self.parse_unit_choice.GetString(index)) //8)
            temp_value = temp_value // int(self.parse_number_textCtrl.GetValue())
            self.max_loop_textCtrl.SetValue(str(temp_value))
            self.max_loop_textCtrl.Disable()

        else:
            self.parse_check_button.Disable()
            self.max_loop_textCtrl.Enable()
            self.max_loop_textCtrl.Clear()

    '''
    excel check button 按下的handler function
    '''
    def excel_check( self, event):
        global excel_file
        global excel_dict

        excel_file.open_sheet(self.sheet_choice.GetCurrentSelection())
        #从起始行开始进行一整行的读取,判断是否有关键字
        excel_file.format_check(excel_file.sheet,
                                int(self.startrow_textCtrl.Value),
                                1)

        if (excel_file.sheet_valid):
            dlg = wx.MessageDialog(None, "excel 文件格式正确")
            retCode = dlg.ShowModal()
            dlg.Destroy()

        else:
            dlg = wx.MessageDialog(None, "excel 文件格式错误,请检查文件格式！")
            retCode = dlg.ShowModal()
            self.excel_check_button.Disable()
            dlg.Destroy()

        if (excel_file.sheet_valid):
            self.m_statusBar.PushStatusText("excel reading...", field=0)
            excel_dict = excel_file.sheet_cell_process(excel_file.sheet,
                                                    int(self.startrow_textCtrl.Value),
                                                    int(self.endrow_textCtrl.Value),
                                                    self.m_statusBar)
            #excel_file.save(excel_file.wb)
            excel_file.close(excel_file.wb)
            self.m_statusBar.PushStatusText("excel read done!", field = 0)
        #关闭
        #excel_file.close(excel_file.wb)

    def binary_check(self,event):
        global  data_dict
        global  loop_time
        global  loop_range

        data_dict.clear()  # 每次读取要清除
        #step1: 检查应该设置的值是否正确设置了

        #step2: 如果都设置了，则进行二进制文件的读取和解析
        b_file = Binary_File(self.binary_filePicker.GetPath())
        index = self.parse_unit_choice.GetSelection() #获取选择项
        if (self.loop_checkBox.IsChecked()):
            loop_time = int(self.loop_textctrl.Value)
        else:
            loop_time = 1

        #计算的是单次循环的字节数
        self.m_statusBar.PushStatusText("binary reading...", field=1)
        loop_range = int(self.parse_number_textCtrl.Value) * int(self.parse_unit_choice.GetString(index)) // 8
        data_dict = b_file.Binary_file_read_and_unpack(self.parse_unit_choice.GetString(index),
                                            self.parse_number_textCtrl.Value,
                                            self.loop_checkBox.IsChecked(),
                                            self.loop_textctrl.Value,
                                            self.ending_choice.GetCurrentSelection())
        self.m_statusBar.PushStatusText("binary read done!{0}-{1}".format(len(data_dict), loop_time), field=1)
        pass





    '''
     output data format choice
    '''
    def output_data_format( self, event ):
        global parse_data_format
        if (self.output_data_format_choice.GetCurrentSelection() == 0): #16进制
            parse_data_format = 16
        else:
            parse_data_format = 10
            

    '''
    apply button 的解析主处理函数
    '''
    def apply_parse_function( self, event ):
        global excel_dict
        global data_dict
        global loop_time
        global loop_range
        global  output_pat
        
        #读取二进制文件，将读取二进制文件放在apply一起，防止修改之后不重新读取
        data_dict.clear() #每次读取要清除
        # step1: 检查应该设置的值是否正确设置了

        # step2: 如果都设置了，则进行二进制文件的读取和解析
        b_file = Binary_File(self.binary_filePicker.GetPath())
        index = self.parse_unit_choice.GetSelection()  # 获取选择项
        if (self.loop_checkBox.IsChecked()):
	        loop_time = int(self.loop_textctrl.Value)
        else:
	        loop_time = 1

        # 计算的是单次循环的字节数
        self.m_statusBar.PushStatusText("binary reading...", field=1)
        loop_range = int(self.parse_number_textCtrl.Value) * int(self.parse_unit_choice.GetString(index)) // 8

        data_dict = b_file.Binary_file_read_and_unpack(self.parse_unit_choice.GetString(index),
                                                       self.parse_number_textCtrl.Value,
                                                       self.loop_checkBox.IsChecked(),
                                                       self.loop_textctrl.Value,
                                                       self.ending_choice.GetCurrentSelection())
        self.m_statusBar.PushStatusText("binary read done!{0}-{1}".format(len(data_dict) //loop_time,loop_time), field=1)
        pass

        

        #解析之后的每个域段的结果放在excel_dict中的cell_parse_result_list 中
        self.m_statusBar.PushStatusText("parse start", field=2)
        excel_parse_process(excel_dict,
                             data_dict,
                            int(self.parse_number_textCtrl.Value),
                            loop_time,
                            loop_range,
                            parse_data_format,
                            self.m_statusBar)
        self.m_statusBar.PushStatusText("parse done", field=2)

        #
        self.m_statusBar.PushStatusText("output start", field=3)
        excel_parse_output(excel_dict,
                           output_path,
                           self.m_statusBar)
        self.m_statusBar.PushStatusText("output done", field=3)
        pass




if __name__ == "__main__":
    app = wx.App()
    frame = myframe(None)
    frame.Show()
    app.MainLoop()