import wx
import usb_energetics_spy


app = wx.App(False)
frame = usb_energetics_spy.MainFrame()
app.MainLoop()
