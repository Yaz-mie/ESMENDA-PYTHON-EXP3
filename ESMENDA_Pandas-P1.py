#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd

cars = pd.read_csv("Cars.csv") #filename 


# In[7]:


print(cars.head())#first five rows
print(cars.tail())#last five rows

