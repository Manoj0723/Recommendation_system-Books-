#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


# In[2]:


movies = pd.read_csv('movies.csv')
movies.head


# In[3]:


movies.info()


# In[4]:


movies.duplicated().sum()


# In[5]:


movies.tail()


# In[6]:


ratings = pd.read_csv('ratings.csv')
ratings.head()


# In[7]:


ratings.info()


# In[8]:


ratings.duplicated().sum()


# In[9]:


ratings.tail()


# In[10]:


len(ratings['userId'].unique())


# In[39]:


merged_df = pd.merge(movies,ratings, on='movieId')
merged_df.head()


# In[40]:


merged_df.drop(['genres','timestamp'], axis =1,inplace=True)
merged_df.head()


# ## Create a user ID matrix

# In[37]:


user_movie_matrix = merged_df.pivot_table(index='userId',columns='title',values='rating')
user_movie_matrix


# In[14]:


user_movie_matrix.fillna(0, inplace=True)
user_movie_matrix.head()


# # Cosine similarity

# In[15]:


user_similarity_matrix = cosine_similarity(user_movie_matrix)
user_similarity_matrix 


# In[16]:


type(user_similarity_matrix )


# In[17]:


np.fill_diagonal(user_similarity_matrix , 0)


# In[18]:


user_similarity_df = pd.DataFrame(user_similarity_matrix , columns = ratings['userId'].unique(),index = ratings['userId'].unique())
user_similarity_df.head()


# ## Make recommendations for user id 3

# In[19]:


user_id = 3


# In[20]:


user_similarity_df[user_id]


# ### Users most similiar to User3

# In[21]:


user_similarity_df[user_id].sort_values(ascending=False)[:3].index


# In[22]:


user_movie_matrix.loc[313]


# In[23]:


user_movie_matrix.loc[313].sort_values(ascending = False)


# In[24]:


user_movie_matrix.loc[313].sort_values(ascending = False).index[:3]


# In[25]:


user_movie_matrix.loc[377]


# In[26]:


user_movie_matrix.loc[377].sort_values(ascending = False).index[:3]


# In[27]:


user_movie_matrix.loc[532]


# In[28]:


user_movie_matrix.loc[532].sort_values(ascending = False).index[:3]


# 
# ## Item Item similiarity

# In[29]:


movie_user_matrix = user_movie_matrix.T
movie_user_matrix


# In[30]:


user_movie_matrix.T


# In[31]:


user_movie_matrix.fillna(0, inplace=True)
user_movie_matrix.head()


# ## cosine similiarity

# In[32]:


user_similarity_matrix = cosine_similarity(user_movie_matrix)
user_similarity_matrix 


# In[33]:


user_similarity_matrix = cosine_similarity(user_movie_matrix)
user_similarity_matrix 


# In[34]:


user_similarity_df = pd.DataFrame(user_similarity_matrix , columns = ratings['userId'].unique(),index = ratings['userId'].unique())
user_similarity_df.head()


# In[35]:


user_id = 3


# In[36]:


user_similarity_df[user_id]


# In[ ]:




