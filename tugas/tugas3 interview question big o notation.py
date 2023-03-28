#!/usr/bin/env python
# coding: utf-8

# # interview question 1

# In[1]:


def foo(array):
    sum = 0
    product = 1
    
    for i in array:
        sum += i
        
    for i in array:
        product *= i
    print("Sum = "+str(sum)+", Product = "+str(product))
    
ar1 = [1,2,3,4]
foo(ar1)


# # interview question 2

# In[4]:


def PrintPairs(array):
    for i in array:
        for j in array:
            print(str(i)+","+str(j))


# # interview question 3

# In[5]:


def printUnorderedPairs(array):
    for i in range(0,len(array)):
        for j in range(i+1,len(array)):
            print(array[i] + "," + array[j])


# # interview question 4

# In[2]:


def printUnorderedPairs(arrayA, arrayB):
    for i in range (len(arrayA)):
        for j in range(len(arrayB)):
            if arrayA[i] < arrayB[j]:
                print(str(arrayA[i]) + "," + str(arrayB[j]))
                
arrayA = [1,2,3,4,5]
arrayB = [2,6,7,8]


# # interview question 5

# In[3]:


def printUnorderedPairs(arrayA, arrayB):
    for i in range (len(arrayA)):
        for j in range(len(arrayB)):
            for k in range(0,100000):
                print(str(arrayA[i]) + "," + str(arrayB[j]))
                
# printUnorderedPairss(arrayA,arrayB)


# # interview question 6

# In[4]:


def reverse(array):
    for i in range(0, int(len(array)/2)):
        other = len(array)-i-1
        temp = array[i]
        array[i] = array[other]
        array[other] = temp
    print(array)
    
reverse(arrayA)


# # interview question 8

# In[5]:


def factorial(n):
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(3))


# # interview question 9

# In[12]:


def allFib(n):
    for i in range(n):
        print(str(i)+":, " + str(fib(i)))
    
def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib (n-2)


# # interview question 10

# In[7]:


def powerOf2(n):
    if n < 1:
        return 0
    elif n == 1:
        print(1)
        return 1
    else:
        prev = powerOf2(int(n/2))
        curr = prev*2
        print(curr)
        return curr
    
powerOf2(50)


# In[ ]:




