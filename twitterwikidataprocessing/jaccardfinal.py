
import xml.etree.cElementTree as ET
import xml.etree.ElementTree as etree
import os
import string
from string import ascii_letters
import io
import re
import csv
import codecs
import datetime
import json, time, sys
import xml.etree.ElementTree as etree
from SPARQLWrapper import SPARQLWrapper, JSON
import wordsegment
from wordsegment import load, segment
import splitter
import enchant, sys
import nltk, re, pprint
from nltk import word_tokenize
#from wordsegmentation import WordSegment
from nltk import ngrams
from nltk.corpus import stopwords
from scipy import stats
from scipy.stats import ks_2samp
import numpy as np
import distance

# Jaccard similarity per string
def jaccard(a,b):
    a=a.split()
    b=a.split()
    union = list(set(a+b))
    intersection = list(set(a) - (set(a)-set(b)))
    print("Union - %s" % union)
    print("Intersection - %s" % intersection)
    jaccard_coeff = float(len(intersection))/len(union)
    print("Jaccard Coefficient is = %f " % jaccard_coeff)

# Jacarta similary of 2 full lists 
def jaccard_similarity(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    print(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection / union)

    
subdir = "graphs"
here = os.path.dirname(os.path.realpath(__file__))
with open('./graphs/wikidatatwitter1.csv', 'r') as f:
#with open('./graphs/wikidatatwitter2.csv', 'r') as f:
#with open('./graphs/wikidatatwitter3.csv', 'r') as f:
#with open('./graphs/wikidatatwitter4.csv', 'r') as f:
        print('#####    TRY ######')
        read = csv.reader(f) 
        filepath = os.path.join(here, subdir, 'jacartadistance1' + '.csv')
        #filepath = os.path.join(here, subdir, 'jacartadistance2' + '.csv')
        #filepath = os.path.join(here, subdir, 'jacartadistance3' + '.csv')
        #filepath = os.path.join(here, subdir, 'jacartadistance4' + '.csv')
        filename=open(filepath, 'w', newline='', encoding="utf-8")
        articlesWriter = csv.writer(filename, quoting=csv.QUOTE_MINIMAL)
        #articlesWriter.writerow(['word'] ['frequency'])
        #word = ''
        #frequency = ''
        for line in read:
            lineitem = line[0]
            lineitem1 = line[1]
            writer = csv.writer(filename, delimiter=',')
            jacartadistance = distance.jaccard(lineitem, lineitem1)
            jaccardsimilarity= jaccard_similarity(lineitem, lineitem1)
            #jaccard2=jaccard(lineitem, lineitem1)
            writer.writerow([lineitem, lineitem1, jacartadistance, jaccardsimilarity])



