# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 19:18:33 2021

@author: Chandru
"""
import pandas as pd
import numpy as np
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')

df = pd.read_csv("answers.csv")
df['time_taken'] = df['at']- df['qt']
df.tags.unique()
df['tags'] = df['tags'].apply(lambda x: x.replace('û','u'))
df.to_csv('slightly_cleaned.csv',index = False)

words = " ".join(df['tags'])
def punctutation_stop(text):
    filtered = []
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    for w in word_tokens:
        if w not in stop_words and w.isalpha():
            filtered.append(w.lower())
    return filtered

words_filtered = punctutation_stop(words)
words_filtered1 = pd.unique(words_filtered).tolist()
words_filtered_df = pd.DataFrame(words_filtered1)
words_filtered_df.to_csv("tags.csv",index = False)


