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



def jaccard(a,b):
    #a=a.split()
    #b=a.split()
    union = list(set(a+b))
    intersection = list(set(a) - (set(a)-set(b)))
    #print("Union - %s" % union)
    #print("Intersection - %s" % intersection)
    jaccard_coeff = float(len(intersection))/len(union)
    print("Jaccard Coefficient is = %f " % jaccard_coeff)





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
        print('#####    TRY ######')
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
        print('#####    TRY ######')
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
        print('#####    TRY ######')
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
        print('#####    TRY ######')
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
        print('#####    TRY ######')
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


#print(getWikidataList())
#print(getTwitterList())

wikidatalist = getWikidataList()
twitterData1 = getTwitterList1()
twitterData2 = getTwitterList2()
twitterData3 = getTwitterList3()
twitterData4 = getTwitterList4()

#########################
#STATS 1  
########################
print('NGRAMS 1')
ks_statistic, p_value = ks_2samp(wikidatalist, twitterData1)
print(ks_statistic)
print(p_value)

print('NGRAMS 2')
ks_statistic, p_value = ks_2samp(wikidatalist, twitterData2)
print(ks_statistic)
print(p_value)


print('NGRAMS 3')
ks_statistic, p_value = ks_2samp(wikidatalist, twitterData3)
print(ks_statistic)
print(p_value)


print('NGRAMS 4')
ks_statistic, p_value = ks_2samp(wikidatalist, twitterData4)
print(ks_statistic)
print(p_value)



#########################
# STATS 2
########################

def jaccard_similarity(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    #print(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection / union)

print('NGRAMS 1')
similarity1 = jaccard_similarity(wikidatalist, twitterData1)
distance1 = (1 - similarity1)
print('JJ similarity')
print(similarity1)
print('JJ distance')
print(distance1)

jaccard(wikidatalist, twitterData1)

print('NGRAMS 2')
similarity2 = jaccard_similarity(wikidatalist, twitterData2)
distance2 = (1 - similarity2)
print('JJ similarity')
print(similarity2)
print('JJ distance')
print(distance2)

jaccard(wikidatalist, twitterData2)

print('NGRAMS 3')
similarity3 = jaccard_similarity(wikidatalist, twitterData3)
distance3 = (1 - similarity3)
print('JJ similarity')
print(similarity3)
print('JJ distance')
print(distance3)

jaccard(wikidatalist, twitterData3)

print('NGRAMS 4')
similarity4 = jaccard_similarity(wikidatalist, twitterData4)
distance4 = (1 - similarity4)
print('JJ similarity')
print(similarity4)
print('JJ distance')
print(distance4)

jaccard(wikidatalist, twitterData4)


#%matplotlib inline
#In [2]:

#x = np.random.uniform(size=1000)
#sigma_x = np.std(x)
#mean_x = x.mean()

#plt.hist(x)
#plt.show()

#In [3]:

#y = x**4
#sigma_y = np.std(y)
#mean_y = y.mean()

#plt.hist(y)
#plt.show()

