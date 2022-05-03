#!/usr/bin/env python
# coding: utf-8

# # Create Digital Clock Using Python
# **Created by Yusuf Arico**
# 
# This is a simple program to create a digital clock using python.

# In[1]:


#import Library
from tkinter import *
from tkinter.ttk import *
from time import strftime


# In[2]:


#Creating UI
root = Tk()
root.title("Digital Clock by Yusuf Arico")


# In[3]:


#Creating Label
label = Label(root, font=('ds-digital', 150), background = 'black', foreground = 'red')
label.pack(anchor='center')


# In[4]:


#Define Clock function
def clock():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, clock)


# In[5]:


clock()
mainloop()


# In[ ]:




