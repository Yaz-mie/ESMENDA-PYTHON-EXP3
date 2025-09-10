#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd

cars = pd.read_csv("Cars.csv") #filename 


# In[12]:


print(cars.head())#first five rows
print(cars.tail())#last five rows


# In[13]:


#Display first five rows with odd-numbered columns
print(cars.iloc[0:5, ::2])

