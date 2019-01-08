import wx
import UI

class myframe(UI.MyFrame):
    def parse_choise_selected( self, event ):
        print(self.parse_choice.GetStringSelection())


if __name__ == "__main__":
    app = wx.App()
    frame = myframe(None)
    frame.Show()
    app.MainLoop()