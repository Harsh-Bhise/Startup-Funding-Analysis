#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df = pd.read_excel('Startup_Funding.xlsx')


# In[4]:


df.info()


# In[5]:


df.head()


# In[6]:


df.describe()


# # Get A List Of Startups Having Industry Vertical As "E-Commerce" Situated In Location "Bengaluru" With Funding Of  "10M" and Above.

# In[7]:


df[(df['Industry Vertical'] == "E-Commerce")&(df['Location']=="Bengaluru")&(df['Amount']>10000000)]['Startup Name']


# # Show The Average Funding For Industry Vertical "ED-Tech" For The year 2019

# In[8]:


dfyear = df[df['Date'].dt.year == 2019]
dfyear[dfyear['Industry Vertical']=='Ed-Tech']['Amount'].mean()


# # Get A List Of Investors For The Startup "Zomato"

# In[9]:


df[df['Startup Name']=='Zomato']['Investors']


# # What Is The Most Common Investment Type ?

# In[10]:


df['Investment Type'].value_counts().head(1)


# # Track The Funding Of The Startup "Unacademy" Over The Years 

# In[11]:


import cufflinks as cf 
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot
init_notebook_mode(connected=True)
cf.go_offline()


# In[12]:


dfun = df[df['Startup Name']=='Unacademy']
dfun.iplot(kind='bar',x='Date',y='Amount')


# # Comapre The Average Funding For Investment Types Series A, SeriesB, Series C, Series D

# In[13]:


dfserA = df[df['Investment Type']=='Series A']['Amount'].mean()
dfserB = df[df['Investment Type']=='Series B']['Amount'].mean()
dfserC = df[df['Investment Type']=='Series C']['Amount'].mean()
dfserD = df[df['Investment Type']=='Series D']['Amount'].mean()
SeriesData = [dfserA,dfserB,dfserC,dfserD]
Serieslabels = 'SeriesA SeriesB SeriesC SeriesD'.split()
Series = pd.DataFrame(data=SeriesData,index=Serieslabels)
Series.index.names=['Series']


# In[14]:


Series.plot.bar(figsize=(10,7),legend=False)


# # Get A List OF Startups Names With Funding OF "1B" And Above 

# In[15]:


df[df['Amount']>=1000000000]['Startup Name'].unique()


# # Get All The Available Data For Startup "Meesho" 

# In[17]:


df[df['Startup Name']=='Meesho']


# # Show The Total Yearly Funding For The Startup "Nykaa"

# In[18]:


dfNykaa = df[df['Startup Name']=='Nykaa']
pd.pivot_table(dfNykaa,index='Date',aggfunc='sum')


# # What Was The Highest One Time Funding

# In[30]:


df[df['Amount']==df['Amount'].max()]


# # What Was The Lowest One Time Funding 

# In[31]:


df[df['Amount']==df['Amount'].min()]


# In[ ]:




