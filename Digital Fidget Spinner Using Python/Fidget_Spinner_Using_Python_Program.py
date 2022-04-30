#!/usr/bin/env python
# coding: utf-8

# # Fidget Spinner With Python
# **Created by Yusuf Arico**
# 
# This is a simple program to create a digital fidget spinner game. To try program (play) just tap the **'spacebar'**

# In[7]:


from turtle import *
state = {'turn':0}
def spinner():
    clear()
    angle = state['turn']/10
    right(angle)
    forward(100)
    dot(150,'red')
    back(100)
    right(120)
    forward(100)
    dot(150,'green')
    back(100)
    right(120)
    forward(100)
    dot(150,'blue')
    back(100)
    right(120)
    update()
def animate():
    if state['turn']>0:
        state['turn']-=1
    spinner()
    ontimer(animate, 20)
def flick():
    state['turn']+=10
setup(500,500,370,0)
hideturtle()
tracer(False)
width(20)
onkey(flick, 'space')
listen()
animate()
done()


# In[ ]:




