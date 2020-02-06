#!/usr/bin/env python
# coding: utf-8

# # USB Energetics: Curve display
# Sources: https://drive.google.com/drive/folders/1IPuoeFoGdovOt414OH5nLNP-8nOfWGTN
# 
# Begun the 03/02/2020

# ## Importing the data

# In[1]:


import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.dates as dates
from matplotlib.dates import DateFormatter
import sys
import wx


# ## Put the data in lists

# In[2]:


t=[]
# Creating an empty dictionary 
Data = {} 
  # Adding list as value 
Data["voltage1"] = [] 
Data["voltage2"]=[]
Data["current1"]=[]
Data["current2"]=[]
Data["power1"]=[]
Data["power2"]=[]

#file_path = "C:/Users/TonyTony/Desktop/env/MOR/Task2/332PM_GapA.txt"
file_path = r'C:\Users\TonyTony\Documents\Polytech\Projet_2020_IESE5_USB-Energetics'.replace('\\', '/')
print(file_path)

file_path = file_path + '/2020/1/31.TXT'
print(file_path)
with open(file_path) as file_obj: # we open the file (we don't need to use file.close(), it is automated)
    # split : delete characters in the string mentionned in paramater of split
    # strip: delete beginning and ending characters in parameter
    # file_obj.readline()#permit to jump this line
       for line in file_obj:
            hour, minute, second, volt1, cur1, pow1, volt2, cur2, pow2 = line.strip().split()
            datetime_str=hour+":"+minute+":"+second
            datetime_obj = dt.datetime.strptime(datetime_str, '%H:%M:%S')
            time = dates.date2num(datetime_obj)
            #t.append(3600*int(hour) + 60*int(minute) + int(second))
            t.append(time)
            Data["voltage1"].append(volt1)
            Data["voltage2"].append(volt2) 
            Data["current1"].append(cur1) 
            Data["current2"].append(cur2) 
            Data["power1"].append(pow1) 
            Data["power2"].append(pow2) 
            #voltage1.append(volt1)
            #voltage2.append(volt2)
            #current1.append(cur1)
            #current2.append(cur2)
            #power1.append(pow1)
            #power2.append(pow2)
            if 'str' in line:
                break


# ## Plot figures

# In[3]:


#x is time, y is a dictionnary
#Create a figure which is a subplot of the initial one
def figures(fig,nb_rows,nb_columns,index,x,key,value):
    ax = fig.add_subplot(nb_rows, nb_columns, index)
    plt.plot_date(x, value) #like plot but with data which is date
    #ax.text(x=0.5,y=0.5,s="test")
    plt.ylabel(key)
    plt.xlabel('Time')
    plt.title("31 of January 2020")
    ax.xaxis.set_major_formatter(DateFormatter('%H:%M:%S'))


fig = plt.figure(figsize=(10,20))
n=6
index = 1
for key,value in Data.items():
    
    figures(fig,3,2,index,t,key,value)
    index+=1

fig.tight_layout() #adjust the space between the different subplots
plt.show()


#test
app=[]
app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
frame = wx.Frame(None, wx.ID_ANY, "Hello World") # A Frame is a top-level window.
frame.Show(True)     # Show the frame.
app.MainLoop()