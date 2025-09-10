#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

cars = pd.read_csv("Cars.csv") #filename 


# In[2]:


print(cars.head())#first five rows
print(cars.tail())#last five rows


# In[3]:


#Display first five rows with odd-numbered columns
print(cars.iloc[0:5, ::2])


# In[4]:


#Row containing model 'Mazda RX4'
print(cars[cars["Model"] == "Mazda RX4"])


# In[5]:


#Cylinders of 'Camaro Z28'
print(cars.loc[cars["Model"] == "Camaro Z28", "cyl"])


# In[6]:


#Cylinders and gear type of multiple models
models = ["Mazda RX4 Wag", "Ford Pantera L", "Honda Civic"]
print(cars.loc[cars["Model"].isin(models), ["Model", "cyl", "gear"]])

