#!/usr/bin/env python
# coding: utf-8

# In[4]:


import math
def binarySearch(array, value):
    start = 0
    end = len(array)-1
    middle = math.floor((start+end)/2)
    while not(array[middle]==value) and start<=end:
        if value < array[middle]:
            end = middle - 1
        else:
            start = middle + 1 
        middle = math.floor((start+end)/2)
        # print(start, middle, end)
    if array[middle] == value:
        return middle
    else:
        return -1


# In[5]:


custArray = [8, 9, 12, 15, 17, 19, 20, 21, 28]


# In[6]:


print(binarySearch(custArray, 15))


# In[7]:


# [8, 9, 12, 15, 17, 19, 20, 21, 28]
#  S              M               E
#  S  M      E
#        SM  E
#            SME


# In[ ]:




