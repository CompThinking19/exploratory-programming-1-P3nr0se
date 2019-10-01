#!/usr/bin/env python
# coding: utf-8

# In[2]:

#defining 'double' which is intended to multiply by two
def double(sequence):
    result = []
    for element in sequence:
        result = result + [element * 2]
    return result


# In[4]:

#attempt to multiply variable by two
double([4])


# In[5]:

#defining 'quadruple' which is intended to multiply variables by four
def quadruple(sequence):
    result = []
    for element in sequence:
        result = result + [element * 4]
    return result


# In[6]:

#first attempt to multiply listed numbers by four
quadruple([1,3,5,7,9])


# In[7]:

#second attempt to multiply list by four
quadruple([2,4,6,8,10])


# In[10]:

#attempt to multiply by four, with non integer variable
quadruple([100,200,300,'you guys are gonna make me rich! '])
# Notably, I do not know how to run things in Atom, but when called, the sequence does run in Jupyter.

# In[ ]:
