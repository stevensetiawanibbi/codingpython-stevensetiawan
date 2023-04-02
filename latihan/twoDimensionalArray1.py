#!/usr/bin/env python
# coding: utf-8

# In[39]:


import numpy as np


# In[40]:


twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDArray)


# In[41]:


newTwoDArray = np.insert(twoDArray, 1, [[1,2,3,4]], axis=0)
print(newTwoDArray)


# In[42]:


print(len(twoDArray))


# In[43]:


newTwoDArray = np.append(twoDArray, [[1,2,3,4]], axis=0)
print(newTwoDArray)


# In[44]:


print(len(newTwoDArray))


# In[45]:


print(len(newTwoDArray[0]))


# In[46]:


def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) or colIndex >= len(array[0]):
        print('Incorrect Index')
    else:
        print(array[rowIndex][colIndex])


# In[47]:


accessElements(newTwoDArray, 1, 2)


# In[48]:


def traverseTDArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])


# In[49]:


traverseTDArray(twoDArray)


# In[50]:


def searchTDArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'The value is located index '+str(i)+" "+str(j)
    return 'The element no found'


# In[51]:


print(twoDArray)


# In[52]:


print(searchTDArray(twoDArray, 12))


# In[53]:


newTDArray = np.delete(twoDArray, 2, axis=0)
print(newTDArray)


# In[54]:


print(twoDArray)


# In[ ]:




