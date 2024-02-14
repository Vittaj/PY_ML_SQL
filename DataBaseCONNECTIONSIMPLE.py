#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().system('pip install pymysql')


# In[3]:


import pandas as pd
import seaborn as sns
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
import math
import pymysql
import warnings
warnings.filterwarnings("ignore")
pd.set_option('display.max_column', None)


# In[21]:


dbcon = pymysql.connect(host="localhost",user= "root",password= "root",database= "empex")


# In[17]:


dbcon


# In[31]:


pd.read_sql_query("""select * from emppexdet where empid=121""",dbcon)


# In[33]:


pd.read_sql_query("""select*from emppexdet where ManagerID=321""",dbcon)


# In[39]:


df


# In[42]:


df= pd.read_sql_query("""select * from emppexdet""",
 dbcon)


# In[43]:


df.info()


# In[45]:


df.head()


# In[46]:


df.head(2)


# In[50]:


df.tail(-1)


# In[51]:


df.describe()


# In[53]:


df.shape


# In[54]:


sns.countplot(x="City", data=df)


# In[55]:


sns.pairplot(df, hue="City")


# In[ ]:




