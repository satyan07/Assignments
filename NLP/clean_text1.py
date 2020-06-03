#!/usr/bin/env python
# coding: utf-8

# In[1]:


from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import pandas as pd
import sys

tokenizer = RegexpTokenizer(r'\w+')
en_stopwords = set(stopwords.words('english'))
ps = PorterStemmer()


# In[ ]:


def getStemmedReview(review):
    review = review.lower()
    review = review.replace("<br /><br />", "")
    
    tokens = tokenizer.tokenize(review)
    new_tokens = [token for token in tokens if token not in en_stopwords]
    cleaned_review = [ps.stem(token) for token in tokens]
    cleaned_review = " ".join(cleaned_review)
    return cleaned_review

