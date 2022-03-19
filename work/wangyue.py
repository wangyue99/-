#!/usr/bin/env python
# coding: utf-8

# In[1]:


age = 24
myage = int(age)
print(myage)


# In[2]:


height = 1.72
myheight = float(height)
print(myheight)


# In[3]:


complexNum = 4+3j
print(type(complexNum))


# In[4]:


base =int(input("plz input base:"))
height = int(input("plz input height:"))
area = 0.5*base*height
print(int(area))


# In[5]:


sda =int(input("plz input side a:"))
sdb = int(input("plz input side b:"))
sdc = int(input("plz input side c:"))
perimeter = sda+sdb+sdc
print(int(perimeter))


# In[6]:


print('The perimeter =12,side a =5,side b =4')
sidec = int(input('plz input the length of side c '))
area = sidec*4
print(area)


# In[7]:


radius = int(input('plz input the radius '))
area = 3.14**radius
circumference = 2*3.14*radius
print(int(area))
print(int(circumference))


# In[8]:


import numpy as np
import math
p1=np.array([2,2])
p2=np.array([6,10])
p3=p2-p1
p4=math.hypot(p3[0],p3[1])
print(int(p4))


# In[9]:


p1 = [2, 2]
p2 = [6, 10] 
slope = abs((p1[1] - p2[1]) / (p1[0] - p2[0] + 1e-5)) 
print(int(slope))


# In[10]:


from sympy import *
x = symbols('x')
print(solve(6*x+x*x+9,x))


# In[11]:


len(str('python'))


# In[12]:


len(str('python'))


# In[13]:


len(str('python'))>len(str('python'))


# In[14]:


a = 'I hope this course is not full of jargon.'
if 'jargon' in a:
    print('true')
else:
    print(flase)


# In[15]:


print(str(float(len(str('python')))))


# In[16]:


num =int( input('?:'))
if num % 2 == 0:
    print('even')

else:
     print('odd')


# In[17]:


7/3 ==2.7


# In[18]:


type('10') == type(10)


# In[ ]:




