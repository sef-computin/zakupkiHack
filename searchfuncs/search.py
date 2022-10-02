import os
import gensim
import re
from gensim import models
import numpy as np
from gensim.utils import simple_preprocess
from gensim import corpora
import gensim.downloader as api
from multiprocessing import cpu_count
from gensim.models import Word2Vec
from nltk.corpus import stopwords
from pymorphy2 import MorphAnalyzer
import pprint
from gensim import similarities
from collections import defaultdict
import nltk
from pymorphy2 import MorphAnalyzer

'''
nltk.download('averaged_perceptron_tagger_ru')
nltk.download('stopwords')
'''

morph = MorphAnalyzer()

patterns = "[!#$%&'()*+,./:;<=>?@[\]^_`{|}~—\"\-]+"

doc = open('Контракты 44ФЗ финал.txt', encoding = 'utf-8')
buff = []
for sentence in doc.read().split('\n'):
    buff.append(sentence)

doc.close()

text_corpus = []

for token in buff:
    token = re.sub(r'[^\w\s]', '', token)
    text_corpus.append(token)

print(text_corpus)


#stoplist = set('и или в на за из , ; : ! ? ( )'.split(' '))
#functors_pos = {'CONJ', 'ADV-PRO', 'CONJ', 'PART'}
stopwords_ru = stopwords.words("russian")
texts = [[word for word in document.lower().split() if word not in stopwords_ru]
         for document in text_corpus]


frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

processed_corpus = [[token for token in text if frequency[token] > 1] for text in texts]

dictionary = corpora.Dictionary(processed_corpus)

bow_corpus = [dictionary.doc2bow(text) for text in processed_corpus]

tfidf = models.TfidfModel(bow_corpus)

index = similarities.SparseMatrixSimilarity(tfidf[bow_corpus], num_features=842)

query_document = 'обувь с верхом'.split()
query_bow = dictionary.doc2bow(query_document)
sims = index[tfidf[query_bow]]
'''''
print(list(enumerate(sims)))

my_dictionary = corpora.Dictionary(tokenized)

bow_corpus =[my_dictionary.doc2bow(doc, allow_update = True) for doc in tokenized]

tfIdf = models.TfidfModel(bow_corpus, smartirs ='ntc')
weight_tfidf =[]
for doc in tfIdf[bow_corpus]:
    for id, freq in doc:
        weight_tfidf.append([my_dictionary[id], np.around(freq, decimals=3)])

print(weight_tfidf)
'''
