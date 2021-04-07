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

df['unet'] = df["tags"].apply(lambda x: 1 if 'unet' in x.lower() else 0)
df['python'] = df["tags"].apply(lambda x: 1 if 'python' in x.lower() else 0)
df['php'] = df['tags'].apply(lambda x: 1 if 'php' in x.lower() else 0)
df['mysql'] = df['tags'].apply(lambda x: 1 if 'sql' in x.lower() else 0)
df['server'] = df['tags'].apply(lambda x: 1 if 'server' in x.lower() else 0)
df['javascript'] = df['tags'].apply(lambda x:1 if 'javascript' in x.lower() else 0)
df['jquery'] = df['tags'].apply(lambda x:1 if 'jquery' in x.lower() else 0)
df['subjective'] = df['tags'].apply(lambda x:1 if 'subjective' in x.lower() else 0)
df['visualstudio'] = df['tags'].apply(lambda x:1 if 'visualstudio' in x.lower() else 0)
df['css'] = df['tags'].apply(lambda x:1 if 'css' in x.lower() else 0)
df['html'] = df['tags'].apply(lambda x:1 if 'html' in x.lower() else 0)
df['database'] = df['tags'].apply(lambda x:1 if 'database' in x.lower() else 0)
df['window'] = df['tags'].apply(lambda x:1 if 'window' in x.lower() else 0)
df['ajax'] = df['tags'].apply(lambda x:1 if 'ajax' in x.lower() else 0)
df['ruby'] = df['tags'].apply(lambda x: 1 if 'ruby'in x.lower() else 0)
df['java'] = 0
df.loc[df.javascript == 0, "java"] = df['tags'].apply(lambda x: 1 if 'java' in x.lower() else 0)
df['eclipse'] = df['tags'].apply(lambda x: 1 if 'eclipse' in x.lower() else 0)
df['iphone'] = df['tags'].apply(lambda x: 1 if 'iphone' in x.lower() else 0)
df['django'] = df['tags'].apply(lambda x: 1 if 'django' in x.lower() else 0)
df['algorithm'] = df['tags'].apply(lambda x: 1 if 'algorithm' in x.lower() else 0)
df['programming'] = df['tags'].apply(lambda x: 1 if 'programming' in x.lower() else 0)
df['lisp'] = df['tags'].apply(lambda x: 1 if 'lisp' in x.lower() else 0)
df['clojure'] = df['tags'].apply(lambda x: 1 if 'clojure' in x.lower() else 0)
df['swing'] = df['tags'].apply(lambda x: 1 if 'swing' in x.lower() else 0)
df['oracle'] = df['tags'].apply(lambda x: 1 if 'oracle' in x.lower() else 0)
df['ruby'] = df['tags'].apply(lambda x: 1 if 'ruby' in x.lower() else 0)
df['lua'] = df['tags'].apply(lambda x: 1 if 'lua' in x.lower() else 0)
df['web-development'] = df['tags'].apply(lambda x: 1 if 'web-development' in x.lower() else 0)
df['c#'] = df['tags'].apply(lambda x: 1 if 'c#' in x.lower() else 0)
df['svn'] = df['tags'].apply(lambda x: 1 if 'svn' in x.lower() else 0)
df['design'] = df['tags'].apply(lambda x: 1 if 'design' in x.lower() else 0)
df['source-code'] = df['tags'].apply(lambda x: 1 if 'source-code' in x.lower() else 0)
df['linux'] = df['tags'].apply(lambda x: 1 if 'linux' in x.lower() else 0)
df['c++'] = df['tags'].apply(lambda x: 1 if 'c++' in x.lower() else 0)
df['open-source'] = df['tags'].apply(lambda x: 1 if 'open-source' in x.lower() else 0)
df['not-programming'] = df['tags'].apply(lambda x: 1 if 'not-programming' in x.lower() else 0)
df['object-oriented'] = df['tags'].apply(lambda x: 1 if 'object-oriented' in x.lower() else 0)
df['ubuntu'] = df['tags'].apply(lambda x: 1 if 'ubuntu' in x.lower() else 0)
df['delphi'] = df['tags'].apply(lambda x: 1 if 'delphi' in x.lower() else 0)
df['conditional'] = df['tags'].apply(lambda x: 1 if 'conditional' in x.lower() else 0)

df['array'] = df['tags'].apply(lambda x: 1 if 'array' in x.lower() else 0)
df['game-development'] = df['tags'].apply(lambda x: 1 if 'game-development' in x.lower() else 0)
df['excel'] = df['tags'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df['career-devleopment'] = df['tags'].apply(lambda x: 1 if 'career-devleopment' in x.lower() else 0)
df['multi-threading'] = df['tags'].apply(lambda x: 1 if 'multi-threading' in x.lower() else 0)
df['interview-questions'] = df['tags'].apply(lambda x: 1 if 'interview-questions' in x.lower() else 0)
df['software-development'] = df['tags'].apply(lambda x: 1 if 'software-development' in x.lower() else 0)
df['debugging'] = df['tags'].apply(lambda x: 1 if 'debugging' in x.lower() else 0)
df['data-structures'] = df['tags'].apply(lambda x: 1 if 'data-structures' in x.lower() else 0)

df.to_csv("Top_Tags_Binary.csv")

from collections import Counter
data = Counter(words_filtered)
tag_count = pd.DataFrame.from_dict(data,orient='index').reset_index()
tag_count.to_csv('tag_count.csv')
