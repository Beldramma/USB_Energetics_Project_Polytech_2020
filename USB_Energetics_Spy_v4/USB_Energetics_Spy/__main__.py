import wx
import USB_Energetics_Spy


app = wx.App(False)
frame = usb_energetics_spy.MainFrame()
app.MainLoop()
