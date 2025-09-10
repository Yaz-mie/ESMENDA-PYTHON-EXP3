#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd

cars = pd.read_csv("Cars.csv") #filename 


# In[14]:


print(cars.head())#first five rows
print(cars.tail())#last five rows


# In[15]:


#Display first five rows with odd-numbered columns
print(cars.iloc[0:5, ::2])


# In[16]:


#Row containing model 'Mazda RX4'
print(cars[cars["Model"] == "Mazda RX4"])

