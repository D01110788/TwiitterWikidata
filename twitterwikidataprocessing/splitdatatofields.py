
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


def process_text(text): 
    text = text.lower()
    text = text.replace('(', '')
    text = text.replace(')', '')
    text = text.replace(',', '')
    text = text.replace("'", '')
    return text.split()


subdir = "graphs"
here = os.path.dirname(os.path.realpath(__file__))

#with open('./wikidataprocessed/order.20190613-130019.csv', 'r') as f:
with open('..\wikidata\processwikidata\wikidataprocessed\order20190613-130019.csv', 'r') as f:
        print('#####    TRY ######')
        read = csv.reader(f) 
        filepath = os.path.join(here, subdir, 'wikidatafinal' + '.csv')
        filename=open(filepath, 'w', newline='', encoding="utf-8")
        articlesWriter = csv.writer(filename, quoting=csv.QUOTE_MINIMAL)

        for line in read:
            lineitem = line[0].split()[0]
            lineitem1 = line[0].split()[1]
            item1 = process_text(lineitem)
            item2 = process_text(lineitem1)
            writer = csv.writer(filename, delimiter=',')
            writer.writerow([item1[0], item2[0]])



