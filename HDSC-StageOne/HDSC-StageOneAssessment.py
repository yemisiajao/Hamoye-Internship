#!/usr/bin/env python
# coding: utf-8

# In[6]:


#import python libraries

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[4]:


#read the fuel dataset
fuel_data = pd.read_csv('fuel_ferc1.csv')
fuel_data


# In[19]:


#Question 3: Which of the fuel type code has the lowest average fuel cost per unit burned?

fuel_data.groupby('fuel_type_code_pudl')['fuel_cost_per_unit_delivered'].count()


# In[5]:


#still on question 3: I visualized the data to have a clearer glimpse

plt.xlabel("Fuel type")
plt.ylabel("Fuel cost per unit burned")
plt.bar(fuel_data.fuel_type_code_pudl, fuel_data.fuel_cost_per_unit_burned)


# In[4]:


#question 4: what is the standard deviation and 75th percentile of the measure of energy per unit (fuel_mmbtu_per_unit) in two decilmal places?

#get a statistical summary of the dataset
fuel_data.describe(include='all')


# In[11]:


# question 5: What is the skewness and kurtosis for the fuel quantity burned in two decimal places?

#using the scipy library
from scipy.stats import skew
from scipy.stats import kurtosis


# In[9]:


print('skew :', skew(fuel_data['fuel_qty_burned']))


# In[12]:


print('kurtosis :', kurtosis(fuel_data['fuel_qty_burned']))


# In[11]:


# Question 6: Which feature has missing values and what is the total number of missing value 
# and percentage of the missing rows as a factor of the total number of rows in three decimal places? 
#(Enter answer in the format: Feature: xxx, Total: xxx, Percent: xxx)


# In[14]:


#check for missing values
missing_values = fuel_data.isnull().sum()
print(missing_values)


# In[70]:


# to get the percentage of missing values
# divide the total missing values in the feature with missing value by the total number of rows in the dataset and multiply by 100 

fuel_unit_missingtotal = fuel_data.fuel_unit.isnull().sum()
rows_total = len(fuel_data)

missing_percentage = (fuel_unit_missingtotal/rows_total)*100

# round up to 3 decimal places using round
print("Feature: fuel_unit, Total: 180, Percent: {}%" .format(missing_percentage.round(3)))

#print(missing_percentage)


# In[35]:


# Question 8: Which of the features has the second and third lowest correlation with the Fuel Cost Per Unit Burned?

#to check correlation, I described all the numerical values in the data
check_correl_data = fuel_data.select_dtypes(include=['int', 'float'])
check_correl_data

#comparing the correlation using fuel Cost Per Unit Burned
check_correl = check_correl_data.corr()['fuel_cost_per_unit_burned'][:]

#correlation = (check_correl[abs(check_correl)> 0.0])
correlation = (check_correl[abs(check_correl) > 0.0]).sort_values(ascending=False)
print(correlation)


# In[66]:


# Question 9: For the fuel type coal, what is the percentage change in the fuel cost per unit burned in 1998 compared to 1994?


# In[65]:


# Question 10:  whuch year has the highest average fuel cost per unit delivered?

#group by report_year and get the mean
fuel_data.groupby('report_year')['fuel_cost_per_unit_delivered'].mean()


# In[36]:


#The feature with missing values falls under what category? What missing value imputation technique would you use?


# In[ ]:




