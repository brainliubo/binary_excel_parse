import wx

class IntValidator(wx.Validator):# 创建验证器子类
    def __init__(self):
        wx.Validator.__init__(self)

    def Clone(self):
        return IntValidator()

    def Validate(self):
        textCtrl = self.GetWindow()
        text = textCtrl.GetValue()
        try:
            if text.isnumeric():
                return  True
            else:
                wx.MessageBox("请输入数字","error")
                return False
        except Exception as error:
            print(error)
            pass

    def Validate_MaxLimit(self,max_number):  # 1 使用验证器方法
        textCtrl = self.GetWindow()
        text = textCtrl.GetValue()
        print(text)
        try:
            if text.isnumeric():
                if (int(text) > int(max_number)):
                    wx.MessageBox("循环解析次数不能超出最大循环次数", "Error")
                else:
                    pass
                textCtrl.Refresh()
                print("ture")
                return True
            else:
                wx.MessageBox("请输入正确的数字", "Error")
                textCtrl.SetFocus()
                textCtrl.Refresh()
                print("false")
                return False
        except Exception as err :
            print(err)
            pass


    def Validate_MaxNum(self,max_number):
        textCtrl = self.GetWindow()
        text = textCtrl.GetValue()



    def TransferToWindow(self):
        return True

    def TransferFromWindow(self):
        return True