#!/usr/bin/env python
# coding: utf-8

# In[14]:


shoppingList = ['milk', 'Cheese', 'Butter']


# In[15]:


for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i]+"+"
    print(shoppingList[i])
empty = []
for i in empty:
    print("I am Empty")


# In[16]:


myList = [1,2,3,4,5,6,7]
print(myList)


# In[17]:


myList.insert(4,15)
print(myList)


# In[18]:


myList.append(55)
print(myList)


# In[19]:


newList = [11,12,13,14]
myList.extend(newList)
print(myList)


# In[20]:


myList = [10,20,30,40,50,60,70,80,90]

def searchinList(list, value):
    for i in list:
        if i == value:
            return list.index(value)
    return 'The value does not exist in the list'

print(searchinList(myList, 60))


# In[21]:


print(myList)


# In[22]:


total = 0
count = 0
while (True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count = count + 1
    average = total / count

print('Average:', average)


# In[24]:


numList = list()
while (True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    numList.append(value)
    
average = sum(numList) / len(numList)
print('Average:', average)


# In[ ]:




