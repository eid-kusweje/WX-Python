import wx

class MyFrame(wx.Frame):
    def _init_(self):
        super()._init_(parent=None, title='Hello World')
        panel = wx.Panel(self)

        # Static text (non-editable label)
        self.label = wx.StaticText(panel, label='Whats your name:', pos=(5, 10))

        # Text box
        self.text_ctrl = wx.TextCtrl(panel, value='initial text', pos=(120, 5))

        # Button
        self.my_btn = wx.Button(panel, label='Press Me', pos=(5, 35))

        # Radio buttons
        self.radio1 = wx.RadioButton(panel, label='Male', pos=(5, 70), style=wx.RB_GROUP)
        self.radio2 = wx.RadioButton(panel, label='Female', pos=(5, 90))

        # Check box
        self.checkbox = wx.CheckBox(panel, label='I agree', pos=(5, 115))

        #combobx
        self.combobox=wx.ComboBox(panel,choices= ['Nsima','Meat', 'Soya', 'Rice'],  pos=(5, 130))

        #text slider
        self.slider = wx.Slider(panel, value=50,minValue=0, maxValue=100, pos=(5, 150),size=(250, -1))

        self.Show()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()