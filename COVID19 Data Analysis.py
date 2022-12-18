#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv(r"C:\Users\Lenovo\Desktop\covid dataset\4. covid_19_data.csv")


# In[3]:


data


# In[4]:


data.count()


# In[6]:


data.isnull().sum()


# In[7]:


import seaborn as sns


# In[8]:


import matplotlib.pyplot as plt


# In[9]:


plt.show()


# In[10]:


sns.heatmap(data.isnull())


# In[11]:


#1 Number of confirmed,deaths and recovered cases in each region


# In[12]:


data.head(2)


# In[14]:


data.groupby('Region').sum().head(20)


# In[20]:


data.groupby('Region')['Confirmed'].sum().sort_values(ascending = False).head(10)


# In[21]:


data.groupby('Region')['Recovered'].sum().sort_values(ascending = False).head(10)


# In[22]:


data.head(2)


# In[ ]:


#2 removing all the records where confirmed cases is less than 10


# In[30]:


data = data[~ data.Confirmed < 10]


# In[31]:


data


# In[33]:


data.head(20)


# In[34]:


data = pd.read_csv(r"C:\Users\Lenovo\Desktop\covid dataset\4. covid_19_data.csv")


# In[35]:


#3 Regions were maxmimum number of cases were recorded


# In[36]:


data.head(2)


# In[37]:


data.groupby('Region').Confirmed.sum().sort_values(ascending = False)


# In[38]:


#4 region where minimum number of deaths were recorded


# In[39]:


data.head(2)


# In[42]:


data.groupby('Region').Deaths.sum().sort_values(ascending = True).head(50)


# In[43]:


#5 How many confirmed, deaths and recovered cases were reported from india till 20 april 2020


# In[44]:


data.head(2)


# In[48]:


data[data.Region == 'India']


# In[49]:


#6 sorting entire data with respect to confirmed cases in ascending order


# In[50]:


data.head(2)


# In[55]:


data.sort_values( by = ['Confirmed'], ascending = True ).head(50)


# In[52]:


#7 sorting entire data with respect to recovered cases in descending order


# In[56]:


data.sort_values(by = ['Recovered'] , ascending = False).head(50)


# In[ ]:





# In[29]:




