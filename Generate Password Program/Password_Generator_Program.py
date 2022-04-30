#!/usr/bin/env python
# coding: utf-8

# # Password Generator Program
# **Created by Yusuf Arico**
# 
# This is simple program to generate password based on the number of characters that we input before.

# In[1]:


import random

passwordinput = int(input("Enter total character: "))

# save alphabets, number, and special characters
container = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*?"

# random sampling by joining the total input characters and container data
rdm = "".join(random.sample(container, passwordinput))
print(rdm)


# In[ ]:




