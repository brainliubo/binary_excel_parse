import wx
import UI
import xlwings
import excel_process  as EP
import os

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
    def excel_check( self, event ):
        excel_file = EP.excel_item(self.excel_filePicker.GetPath())
        excel_dict = {}
        excel_file.read_sheet(0)

        excel_file.format_check(excel_file.sheet, 1, 1)

        excel_dict = excel_file.sheet_cell_process(excel_file.sheet)

        for item in excel_dict:
            print(item)

    def  binary_file_read(self,event):
        self.binary_file_size_textctrl.Value = str(os.path.getsize( self.binay_filePicker.GetPath()))






if __name__ == "__main__":
    app = wx.App()
    frame = myframe(None)
    frame.Show()
    app.MainLoop()