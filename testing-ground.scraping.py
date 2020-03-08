#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd
import sqlalchemy
import pymysql


# In[24]:


dfs = pd.read_html('http://testing-ground.scraping.pro/table')


# In[25]:


df = dfs[0]


# In[26]:


engine = sqlalchemy.create_engine('mysql+pymysql://root:root@localhost:3306/application')


# In[27]:


df.drop([0, 5, 6, 7, 12, 13, 14, 19, 20], axis = 0, inplace=True)


# In[28]:


df.columns = ['quarter', 'product_1_items', 'product_1_amount', 'product_2_items', 'product_2_amount', 'product_3_items', 'product_3_amount', 'total_amount']


# In[29]:


df['product_1_amount'] = df['product_1_amount'].str.replace('$','')
df['product_2_amount'] = df['product_2_amount'].str.replace('$','')
df['product_3_amount'] = df['product_3_amount'].str.replace('$','')
df['total_amount'] = df['total_amount'].str.replace('$','')
df['product_1_amount'] = df['product_1_amount'].str.replace(',','')
df['product_2_amount'] = df['product_2_amount'].str.replace(',','')
df['product_3_amount'] = df['product_3_amount'].str.replace(',','')
df['total_amount'] = df['total_amount'].str.replace(',','')


# In[30]:


df.replace({"-": 0}, inplace = True)


# In[31]:


year = ['2000', '2000','2000', '2000', '2001', '2001', '2001', '2001', '2002', '2002', '2002', '2002']
df['year'] = year


# In[34]:


connection = pymysql.connect(host='localhost',
                         user='root',
                         password='root',
                         db='application')


# create cursor
cursor=connection.cursor()

cols = "`,`".join([str(i) for i in df.columns.tolist()])

# Insert DataFrame recrds one by one.
for i,row in df.iterrows():
    sql = "INSERT INTO `records` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
    cursor.execute(sql, tuple(row))

    # the connection is not autocommitted by default, so we must commit to save our changes
    connection.commit()


# In[ ]:




