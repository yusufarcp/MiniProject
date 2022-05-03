#!/usr/bin/env python
# coding: utf-8

# # Spam Detection
# **Created by Yusuf Arico**
# 
# A Simple Program to detecting spam message. Spam detection means detecting spam messages/emails by understanding text so that you can only receive notifications about messages/emails that important to you. With python, the messages/emails can be categorized as a spam or not.

# In[6]:


# import library
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB


# In[7]:


# import the dataset
df = pd.read_csv("https://raw.githubusercontent.com/amankharwal/SMS-Spam-Detection/master/spam.csv", encoding='latin-1')


# In[8]:


# show data
df.head()


# From this dataset were only need 2 features, **class** and **messages.**

# In[9]:


#filtering data
data = df[["class", 'message']]
data


# ### Split dataset into training and test

# now split this dataset into training and test sets and train the model to detect spam messages:

# In[10]:


x = np.array(data['message'])
y = np.array(data['class'])

cv = CountVectorizer()
X = cv.fit_transform(x) # fit the data
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=42)

clf = MultinomialNB()
clf.fit(X_train, y_train)


# ***we can test the model by input a message like spam to detect whether its spam or not***

# In[18]:


sample = input('Messages:')
data = cv.transform([sample]).toarray()
print(clf.predict(data))


# In[ ]:




