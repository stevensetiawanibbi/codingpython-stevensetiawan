#!/usr/bin/env python
# coding: utf-8

# # Interview question 1

# In[2]:


def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)
n = 123
print(sum_of_digits(n))


# # Interview question 2

# In[3]:


def power(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power(x*x, n//2)
    else:
        return x * power(x*x, (n-1)//2)
x = 2
n = 3
print(power(x, n))


# # Interview question 3

# In[4]:


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
a = 12
b = 8
print(gcd(a, b))


# # Interview question 4

# In[6]:


def decimal_to_binary(n):
    if n == 0:
        return 0
    else:
        return (n % 2) + 10 * decimal_to_binary(n // 2)
n = 164
print(decimal_to_binary(n))


# In[ ]:




