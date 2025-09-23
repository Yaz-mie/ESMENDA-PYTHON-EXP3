#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

cars = pd.read_csv("Cars.csv") #filename 


# In[2]:


#Display first five rows with odd-numbered columns
print(cars.iloc[0:5, ::2])


# In[3]:


#Row containing model 'Mazda RX4'
print(cars[cars["Model"] == "Mazda RX4"])


# In[4]:


#Cylinders and gear type of multiple models
models = ["Mazda RX4 Wag", "Ford Pantera L", "Honda Civic"]
print(cars.loc[cars["Model"].isin(models), ["Model", "cyl", "gear"]])

