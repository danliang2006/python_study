import wx

class HelloFrame(wx.Frame):

    def __init__(self,*args,**kw):
        super(HelloFrame,self).__init__(*args,**kw)

        pn1 = wx.Panel(self)

        st = wx.StaticText(pn1,label="hello world")
        font = st.GetFont()
        font.PointSize +=5
        font = font.Bold()
        st.SetFont(font)

        #create a menu bar
        self.makeMenuBar()

        self.CreateStatusBar()
        self.SetStatusText("welcome to wxPython!")

    def makeMenuBar(self):
        fileMenu = wx.Menu()

        helloItem = fileMenu.Append(-1,"&HELLO....\tCtrl-H",
                                 "help string shown in status bar for this menu item")
        fileMenu.AppendSeparator()

        exitItem = fileMenu.Append(wx.ID_EXIT)

        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu,"&File")
        menuBar.Append(helpMenu,"&Help")

        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU,self.OnHello,helloItem)
        self.Bind(wx.EVT_MENU,self.OnExit,exitItem)
        self.Bind(wx.EVT_MENU,self.OnAbout,aboutItem)

    def OnExit(self,event):
        self.Close(True)

    def OnHello(self):
        wx.MessageBox("hello again from wx")

    def OnAbout(self,event):
        wx.MessageBox("This is a wxPython Hello World sample",
                      "about hello world 2",wx.OK|wx.ICON_INFORMATION)


if __name__ == '__main__':
    app = wx.App()
    frm = HelloFrame(None,title='hdd')
    frm.Show()
    app.MainLoop()