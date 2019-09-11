import numpy as np
import pandas as pd
import nltk
import re
import os
import codecs
from sklearn import feature_extraction
import mpld3
from numpy import genfromtxt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from nltk.stem.snowball import SnowballStemmer

def tokenize_and_stem(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems


stemmer = SnowballStemmer("english")

nltk.download('punkt')
nltk.download('stopwords')

df = pd.DataFrame()

titles = pd.read_csv('titles.txt',delimiter='\t',names=['Title'])
summaries = pd.read_csv('summaries.txt',delimiter='\t',names=['Summary'])

df['Title'] = titles
df['Summary'] = summaries

##print(df.info())

vectorizer = TfidfVectorizer(use_idf=True,stop_words=nltk.corpus.stopwords.words('english'),tokenizer=tokenize_and_stem)
tfidf_matrix = vectorizer.fit_transform(df['Summary'])
terms = vectorizer.get_feature_names()

num_clusters = 8

km = KMeans(n_clusters=num_clusters)

km.fit(tfidf_matrix)

clusters = km.labels_.tolist()

df['Cluster'] = clusters

feature_names = vectorizer.get_feature_names()
dense = tfidf_matrix.todense()
denselist = dense.tolist()

dense_df = pd.DataFrame(denselist, columns=feature_names, index=df['Title'])
s = dense_df[:1]
for column in s.columns:
    print((s[column]))
    
##print(s)
##s[str(s) > 0].sort_values(ascending=False)[:10]

##sorted_df = df.sort_values("Cluster", ascending=True)

##for index, row in sorted_df.iterrows():
##  print(row['Cluster'],row['Title'])