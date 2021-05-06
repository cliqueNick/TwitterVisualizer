#!/usr/bin/env python
# coding: utf-8

# Remesh data visualization skills test  

# Author: Nickolas Lee  

# Date: 2021-05-05  

# In[1]:


import json
import pandas
import altair
from matplotlib import pyplot


# In[2]:


with open("tweet-data-master/data.json", "r") as file:
    data = json.load(file)
    print("The total number of tweets in the data set:")
    print(len(data["tweets"]))


# In[3]:


lengths = pandas.DataFrame([len(tweet["text"]) for tweet in data["tweets"]], columns=['lengths'])


# In[4]:


tags = pandas.DataFrame([len(tweet["hashtags"]) for tweet in data["tweets"]], columns=['tags'])


# In[5]:


likes = pandas.DataFrame([len(tweet["likes"]) for tweet in data["tweets"]], columns=['likes'])


# In[6]:


retweets = dict()
for tweet in data["tweets"]:
    id = tweet["retweet_id"]
    if id is not None:
        if not retweets.__contains__(id):
            retweets[id] = 1
        else:
            retweets[id] += 1
print("The maximum number of retweets was:")
print(max(retweets.values()))
print("The total number of retweets was:")
print(sum(retweets.values()))


# In[7]:


# combine likes and retweets for overall user engagement score
for retweet in retweets.items():
    likes.at[retweet[0], "likes"] += retweet[1]


# In[8]:


# combine the columns
frame = pandas.concat([lengths, tags, likes], axis=1)


# In[9]:


print(frame.describe())


# In[10]:


fig = pyplot.figure()
axes = fig.add_subplot(projection="3d")
axes.scatter(lengths, tags, likes)
axes.set_xlabel("lengths")
axes.set_ylabel("tags")
axes.set_zlabel("likes")
axes.view_init(25, 25)
pyplot.show()


# In[11]:


altair.data_transformers.disable_max_rows()
# load a simple dataset as a pandas DataFrame
altair.Chart(frame).mark_circle().encode(
    x='lengths',
    y='likes',
    color='tags',
    tooltip=['lengths', 'likes', 'tags']
).interactive()


# In[12]:


altair.Chart(frame).mark_circle().encode(
    x='tags',
    y='likes',
    color='lengths',
    tooltip=['lengths', 'likes', 'tags']
).interactive()


# In[13]:


altair.Chart(frame).mark_circle().encode(
    x='tags',
    y='lengths',
    color='likes',
    tooltip=['lengths', 'likes', 'tags']
).interactive()


# In[ ]:




