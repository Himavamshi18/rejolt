#!/usr/bin/env python
# coding: utf-8

# In[1]:


import bs4
from bs4 import BeautifulSoup as bs
import requests


# In[2]:


link='https://www.flipkart.com/samsung-galaxy-f14-5g-goat-green-128-gb/p/itm032d1a69999cc?pid=MOBGNBFNDPGNJ7HY&lid=LSTMOBGNBFNDPGNJ7HYRCCFUH&marketplace=FLIPKART&q=samsung+5g+mobiles&store=tyy%2F4io&spotlightTagId=BestsellerId_tyy%2F4io&srno=s_1_5&otracker=AS_QueryStore_OrganicAutoSuggest_2_17_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_2_17_na_na_ps&fm=search-autosuggest&iid=5d73f435-d468-43af-bc32-6b1632a86b93.MOBGNBFNDPGNJ7HY.SEARCH&ppt=sp&ppn=sp&ssid=ylwhm1ez0g0000001699852558198&qH=18f9c08fc02b3c49'


# In[3]:


page = requests.get(link)


# In[4]:


page.content


# In[5]:


soup = bs(page.content, 'html.parser')
#it gives us the visual representation of data
print(soup.prettify())


# In[6]:


#_1AtVbE col-12-12  B_NuCI  aMaAEs
name=soup.find('span',class_="B_NuCI")
print(name)


# In[7]:


name.text


# In[8]:


#dyC4hf
price=soup.find('div',class_="_30jeq3 _16Jk6d")
print(price)
price.text


# In[9]:


#_3wmLAA  _3LWZlK
parameters=soup.find('div',class_="_3wmLAA")
print(parameters)
parameters.text


# In[10]:


#_3nkT-2
features=soup.find('div',class_="_2o-xpa")
print(features)
features.text


# In[11]:


#_5pFuey  row _3AjFsn _2c2kV- _250Jnj
specification=soup.find('div',class_="_2418kt")
print(specification)
specification.text


# In[12]:


for each in specification:
    spec=each.find_all('li',class_='_21Ahn-')
    print(spec[0].text)
    print(spec[1].text)
    print(spec[2].text)
    print(spec[3].text)


# In[13]:


#_3LWZlK
rating=soup.find('div',class_="_2d4LTz")
print(rating.text)


# In[14]:


products=[]              #List to store the name of the product
prices=[]                #List to store price of the product
ratings=[]               #List to store rating of the product


# In[15]:


products.append(name.text)
prices.append(price.text)
ratings.append(rating.text)


# In[16]:


import pandas as pd
import numpy as np
df = pd.DataFrame(spec)
print(df)


# In[17]:


print(df.isnull())


# In[18]:


print(df.isnull().sum())


# In[19]:


df.dropna(
    axis=0,         # Whether to drop rows or columns
    how='any',      # Whether to drop records if 'all' or 'any' records are missing
    thresh=None,    # How many columns/rows must be missing to drop
    subset=None,    # Which rows/columns to consider
    inplace=False   # Whether to drop in place (i.e., without needing to re-assign)
)


# In[20]:


df = df.dropna()
print(df)


# In[21]:


df = df.dropna(how='all')
print(df)


# In[22]:


df = df.fillna(0)
print(df)


# In[23]:


print(df.duplicated())


# In[24]:


print(df.duplicated().sum())

