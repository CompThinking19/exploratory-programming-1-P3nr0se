#!/usr/bin/env python
# coding: utf-8

# In[2]:


def double(sequence):
    result = []
    for element in sequence:
        result = result + [element * 2]
    return result


# In[4]:


double([4])


# In[5]:


def quadruple(sequence):
    result = []
    for element in sequence:
        result = result + [element * 4]
    return result


# In[6]:


quadruple([1,3,5,7,9])


# In[7]:


quadruple([2,4,6,8,10])


# In[10]:


quadruple([100,200,300,'you guys are gonna make me rich! '])


# In[ ]:




