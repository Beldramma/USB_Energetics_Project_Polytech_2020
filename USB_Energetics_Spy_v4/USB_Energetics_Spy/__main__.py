# -*- coding: utf-8 -*-
#!/usr/bin/python
import wx
from .USB_Energetics_Spy import MainFrame

app = wx.App(False)
frame = MainFrame()

app.MainLoop()
