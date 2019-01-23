import wx
import UI
import xlwings
import excel_process  as EP
import os
from  reg_class import Binary_File
global excel_file


class myframe(UI.MyFrame):
    def parse_choise_selected( self, event ):
        print(self.parse_choice.GetStringSelection())
    def output_excel_changed( self, event ):
        self.excel_output_textctrl.Value = self.output_excel_filePicker.GetPath()
    def loop_parse_check( self, event ):
        if self.loop_checkBox.IsChecked() == True:
            self.loop_textctrl.Enable()
        else:
            self.loop_textctrl.Disable()

    def output_choice_select( self, event ):
        if self.output_choice.GetSelection() == 0:
            #输出excel
            self.output_excel_textctrl.Enable()
            self.output_log_textctrl.Disable()
        else:
            #输出文本文件
            self.output_log_textctrl.Enable()
            self.output_excel_textctrl.Disable()
    '''
    文件选择时的处理
    '''
    def excel_file_select(self,event):
        self.excel_check_button.Disable()
        # disable button ,clear the textctrl's content

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
        self.binary_check_button.Disable()
        self.parse_unit_choice.SetString(0,"")
        self.parse_number_textCtrl.Clear()
        self.loop_textctrl.Clear()
        self.max_loop_textCtrl.Clear()



    '''
    excel check button的使能和去使能
    '''
    def excel_check_button_process( self, event ):
        index = self.sheet_choice.GetSelection()
        print(self.sheet_choice.GetString(index))
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
        if ((self.parse_unit_choice.GetString(index)!= "") and (self.parse_number_textCtrl.GetValue() != "")):
            self.binary_check_button.Enable()
            temp_value = int(self.binary_file_size_textctrl.GetValue()) // (int(self.parse_unit_choice.GetString(index)) //8)
            temp_value = temp_value // int(self.parse_number_textCtrl.GetValue())
            self.max_loop_textCtrl.SetValue(str(temp_value))
            self.max_loop_textCtrl.Disable()

        else:
            self.binary_check_button.Disable()
            self.max_loop_textCtrl.Enable()
            self.max_loop_textCtrl.Clear()

    '''
    excel check button 按下的handler function
    '''
    def excel_check( self, event ):
        global excel_file
        excel_dict = {}
        excel_file.read_sheet(0)

        excel_file.format_check(excel_file.sheet, 1, 1)
        if (excel_file.sheet_valid):
            excel_dict = excel_file.sheet_cell_process(excel_file.sheet,
                                                    int(self.startrow_textCtrl.Value),
                                                    int(self.endrow_textCtrl.Value))
            dlg = wx.MessageDialog(None, "excel 文件格式正确")
            retCode = dlg.ShowModal()
            dlg.Destroy()
        else:
            dlg = wx.MessageDialog(None, "excel 文件格式错误,请检查文件格式！")
            retCode = dlg.ShowModal()
            self.excel_check_button.Disable()
            dlg.Destroy()

    def binary_check(self,event):
        b_file = Binary_File(self.binary_filePicker.GetPath())
        index = self.parse_unit_choice.GetSelection()

        data_dict = b_file.Binary_file_read(self.parse_unit_choice.GetString(index),
                                            self.parse_number_textCtrl.Value,
                                            self.loop_checkBox.IsChecked(),
                                            self.loop_textctrl.Value)
        pass




if __name__ == "__main__":
    app = wx.App()
    frame = myframe(None)
    frame.Show()
    app.MainLoop()