import wx
import UI
import xlwings

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

if __name__ == "__main__":
    app = wx.App()
    frame = myframe(None)
    frame.Show()
    app.MainLoop()