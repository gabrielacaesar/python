
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:

petr4 = pd.read_csv("http://www.google.com/finance/historical?cid=868181216622781&startdate=Aug+28%2C+2016&enddate=Aug+27%2C+2017&num=30&ei=iV-iWbCHIor7mAHT2Y6QAQ&output=csv")


# In[3]:

petr4


# In[4]:

petr4.head()


# In[5]:

petr4.info()


# In[6]:

petr4.Volume


# In[7]:

petr4.Volume.value_counts()


# In[8]:

petr4.Close.value_counts()


# In[9]:

petr4.Open.value_counts()


# In[11]:

petr4.Close.value_counts().reset_index()


# In[ ]:



