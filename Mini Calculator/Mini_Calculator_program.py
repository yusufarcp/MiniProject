#!/usr/bin/env python
# coding: utf-8

# # Mini Calculator Program
# **Created by Yusuf Arico**
# 
# A simple program to create mini calculator using class and function in python.

# In[1]:


#import Library
from tkinter import *


# In[24]:


#define mini calculator function(
class Calc:
    def __init__(self, master):
        self.MathVariable = 0
        self.Value = 0
        self.master = master
        
        self.NumberEntry = Entry(self.master, width=50, borderwidth=5, justify=CENTER)
        self.NumberEntry.grid(row=0, column=0, padx=10,pady=10, columnspan=5)
        i,j=1,0
        for btn in ['1','2','3','4','5','6','7','8','9','+','-','0','*','/','=']:
            if i%4==0:
                i=1
                j+=1
            Button(self.master,text=btn, width=5, command=lambda num =btn:self.BtnClick(num)).grid(row=i, column=j, ipadx=4)
            i+=1
        self.clear = Button(self.master, text='Clear', width=15, command=self.Clear).grid(row=5, columnspan=6, ipadx=70)
        
    def BtnClick(self, number):
        if number == '=':
            self.Equal()
        else:
            self.NumberEntry.insert(len(self.NumberEntry.get()) + 1, str(number))
    
    def Equal(self):
        value1 = self.NumberEntry.get()
        try:
            value1 = eval(value1)
            self.NumberEntry.deleted(0, END)
            self.NumberEntry.insert(0, value1)
        except Exception as e:
            self.NumberEntry.delete(0, END)
            self.NumberEntry.insert(0, e)
            
    def Clear(self):
        self.NumberEntry.delete(0, END)
        self.Value = 0


# In[25]:


# Call for the program
if __name__ == '__main__':
    master = Tk()
    master.title("@yusufarcp Mini Calculator")
   # master.iconbitmap('icon.ico')
    master.geometry('350x200')
    master.resizable(0,0)
    Calc(master)
    master.mainloop()


# # Notes
# 
# **This code can be run, but the mathematical proccess still doesnt work. I will upload this temporarily, will update later when all processes can run. Thank You.**
