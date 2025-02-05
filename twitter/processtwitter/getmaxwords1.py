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
import nltk
from nltk.corpus import stopwords

start_time = time.time()
d2 = datetime.datetime(2019, 3, 15)
d22 = datetime.datetime(d2.year, d2.month, d2.day)
here = os.path.dirname(os.path.realpath(__file__))
subdir = "orderedresults"
bag_of_words = {}

def convert_date_time(dt):
    f = "%Y-%m-%dT%H:%M:%S%fZ"
    dt1 = datetime.datetime.strptime(dt, f)
    dt2 =  datetime.datetime(dt1.year, dt1.month, dt1.day)
    return dt2

def newfilecreation(filename, articlesWriter):
        print('NEW PROCESS')
        articlesWriter = csv.writer(filename, quoting=csv.QUOTE_MINIMAL)
        articlesWriter.writerow(['words'])
        return articlesWriter

def closeoldfile(filename):
        #if counter ==10:
        print(filename)
        filename.flush()
        filename.close()
        time.sleep(5)
        print('SLEEPING')     
        filepath = os.path.join(here, subdir, 'order' + '.' + time.strftime('%Y%m%d-%H%M%S') + '.csv')
        filename=open(filepath, 'w', newline='', encoding="utf-8")
        print(filename)
        print('OPENED')  
        return filename


emptyRow=[]  # Empty lists evaluate to False
words= []

words_counted = []
temp_words_count = []
fileCounter=0

def order_bag_of_words(bag_of_words, desc=False):  
   words = [(word, cnt) for word, cnt in bag_of_words.items()]
   return sorted(words, key=lambda x: x[1], reverse=desc)

def record_word_cnt(word, count, bag_of_words):  
    tempcount = int(count)
    count = 0
    if word != '':
        while(tempcount > 0):
            #print(word)
            #print(tempcount)

            if word.lower() in bag_of_words:
                bag_of_words[word.lower()] += 1
                tempcount-=1
            else:
                bag_of_words[word.lower()] = 1
                tempcount-=1


json_folder_path = os.path.join("count")
# In order to get the list of all files that ends with ".json"
# we will get list of all files, and take only the ones that ends with "json"
json_files = [ x for x in os.listdir(json_folder_path) if x.endswith(".csv") ]
json_data = list()
print(json_files)
for json_file in json_files:
    print('#####    NEW FILE ######')
    print(json_file)
    if (fileCounter == 0 or fileCounter == 5000):
        filepath = os.path.join(here, subdir, 'order' + '.' + time.strftime('%Y%m%d-%H%M%S') + '.csv')
        filename=open(filepath, 'w', newline='', encoding="utf-8")
        articlesWriter = csv.writer(filename, quoting=csv.QUOTE_MINIMAL)
        #articlesWriter.writerow(['word', 'total'])
        #word = ''
        #total = ''
        fileCounter += 1 
    pathWikiXML = os.path.join(json_folder_path, json_file)
    print('##### OPEN NEW FILE ######')
    with open(pathWikiXML, 'r') as f:
        print('#####    TRY ######')
        try:
            fp = csv.reader(f) 
            #cnt = 0
            for line in fp:
                # print(line)
                # replace extra content ["('dem', 20)"]
                line = [word.replace('(','') for word in line]
                line = [word.replace(')','') for word in line]
                line = [word.replace('\'','') for word in line]
                line = [word.replace('"','') for word in line]
                #print(line[0])     
                data = line[0].split(",")  
                #print(data[0])
                #print(data[1])
                record_word_cnt(data[0], data[1], bag_of_words)
                
            sorted_words = order_bag_of_words(bag_of_words, desc=True)
            #print('####### aaaaaa')
            #print(sorted_words)
            #print('####### aaaaaa')
            topwords = sorted_words[:100]
            #print(topwords)
            if fileCounter == 5000:
                print('YES CREATE NEW FILE')
                filename = closeoldfile(filename)
                articlesWriter = newfilecreation(filename, articlesWriter)
                print('GOT OUT OF CREATED FILE')
                fileCounter=0
                #print(filename)
            values = [(value) for value in topwords]
            for item in values:
                row = (
                   item, # count
                  )
                items = [(item) for item in row]
                writer = csv.writer(filename, delimiter=',')
                writer.writerow(items)

        except Exception as ex:
               print(ex)
               print(str(ex)) # for just the message
               print(ex.args) # the arguments that the exception has been called with. 
                  # the first one is usually the message.
       