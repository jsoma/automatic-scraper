#!/usr/bin/env python
# coding: utf-8

# In[12]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[13]:


response = requests.get("https://www.bbc.com/")
doc = BeautifulSoup(response.text, 'html.parser')


# In[14]:


# find everything with the class of media-list__item
# each one of these is going to be a row
stories = doc.select('.media-list__item')

# Starting off without ANY rows
rows = []

for story in stories:
    print("----")
    # Starting off knowing NONE of the columns of data for this datapoint?
    row = {}

    row['title'] = story.select_one('h3').text.strip()

    try:
        # Find me a media__link OR a reel_link
        row['href'] = story.select_one('.media__link, .reel__link')['href']
    except:
        print("Couldn't find a link")

    try:
        row['tag'] = story.select_one('.media__tag').text.strip()
    except:
        print("Couldn't find a tag!")

    try:
        row['summary'] = story.select_one('.media__summary').text.strip()
    except:
        print("Couldn't find a summary")

    print(row)
    # When we're done adding info to our row, we're going to add it into our list
    # of rows
    rows.append(row)


# In[15]:


df = pd.DataFrame(rows)
df


# In[16]:


df.to_csv("bbc-headlines.csv")


# In[ ]:





# In[ ]:




