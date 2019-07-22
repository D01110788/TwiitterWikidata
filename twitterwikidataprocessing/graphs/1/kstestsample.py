#In [1]:

from scipy import stats
from scipy.stats import ks_2samp
import numpy as np
import scipy as sp
import numpy as np
import math
import matplotlib.pyplot as plt
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
    text = text.replace(',', '')
    text = text.replace("'", '')
     # Convert text string to a list of words
    return text.split()


wikidatalist=[]
wikidataset={}

twitterdatalist=[]
twitterdataset={}

def getWikidataList():
    #with open('./wikidataprocessed/order20190613-130019.csv', 'r') as f:
    with open('./SimplifiedList.csv', 'r') as f:
        #print('#####    TRY ######')
        read = csv.reader(f) 
        next(read)
        for line in read:
            lineitem = line[0].split()[0]
            item1 = process_text(lineitem)
            #print(item1[0])
            wikidatalist.append(item1[0])
        #print(wikidatalist)
        wikidataset = set(wikidatalist)
        #print(wikidataset)
        return wikidatalist

def getTwitterList1():
    with open('./orderedresultsngram1/count.csv', 'r') as f:
        #print('#####    TRY ######')
        read = csv.reader(f) 
        next(read)
        for line in read:
            lineitem = line[0].split()[0]
            item1 = process_text(lineitem)
            #print(item1[0])
            twitterdatalist.append(item1[0])
        #print(twitterdatalist)
        #print(set(twitterdatalist))
        twitterdataset = set(twitterdatalist)
        #print(wikidataset)
        return twitterdatalist


def getTwitterList2():
    with open('./orderedresultsngram2/count.csv', 'r') as f:
        #print('#####    TRY ######')
        read = csv.reader(f) 
        next(read)
        for line in read:
            lineitem = line[0].split()[0]
            item1 = process_text(lineitem)
            #print(item1[0])
            twitterdatalist.append(item1[0])
        #print(twitterdatalist)
        #print(set(twitterdatalist))
        twitterdataset = set(twitterdatalist)
        #print(wikidataset)
        return twitterdatalist


def getTwitterList3():
    with open('./orderedresultsngram3/count.csv', 'r') as f:
        #print('#####    TRY ######')
        read = csv.reader(f) 
        next(read)
        for line in read:
            lineitem = line[0].split()[0]
            item1 = process_text(lineitem)
            #print(item1[0])
            twitterdatalist.append(item1[0])
        #print(twitterdatalist)
        #print(set(twitterdatalist))
        twitterdataset = set(twitterdatalist)
        #print(wikidataset)
        return twitterdatalist

def getTwitterList4():
    with open('./orderedresultsngram4/count.csv', 'r') as f:
        #print('#####    TRY ######')
        read = csv.reader(f) 
        next(read)
        for line in read:
            lineitem = line[0].split()[0]
            item1 = process_text(lineitem)
            #print(item1[0])
            twitterdatalist.append(item1[0])
        #print(twitterdatalist)
        #print(set(twitterdatalist))
        twitterdataset = set(twitterdatalist)
        #print(wikidataset)
        return twitterdatalist


wikidatalist = getWikidataList()
twitterData = getTwitterList1()


np.random.seed(12345678)  #fix random seed to get the same result
n1 = len(wikidatalist)  # size of first sample
n2 = len(twitterData)  # size of second sample

# Scale is standard deviation
scale = 3

rvs1 = stats.norm.rvs(wikidatalist, size=n1, scale=scale)
rvs2 = stats.norm.rvs(twitterData, size=n2, scale=scale)
ksresult = stats.ks_2samp(rvs1, rvs2)
ks_val = ksresult[0]
p_val = ksresult[1]

print('K-S Statistics ' + str(ks_val))
print('P-value ' + str(p_val))

rvs1 = stats.norm.rvs(size=n1, loc=0., scale=1)
rvs2 = stats.norm.rvs(size=n2, loc=0.5, scale=1.5)
print(stats.ks_2samp(rvs1, rvs2))





def ks_plot_norm(data):
    length = len(data)
    plt.figure(figsize=(12, 7))
    plt.plot(np.sort(x_100), np.linspace(0, 1, len(x_100), endpoint=False))
    plt.plot(np.sort(stats.norm.rvs(loc=5, scale=3, size=100)), np.linspace(0, 1, len(x_100), endpoint=False))
    plt.legend('top right')
    plt.legend(['Data', 'Theoretical Values'])
    plt.title('Comparing CDFs for KS-Test')
    
ks_plot_norm(x_100)