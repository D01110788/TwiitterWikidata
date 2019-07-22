# !pip install brewer2mpl
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')
import random
import csv
from textwrap import wrap


def process_text(text): 
    text = text.replace('(', '')
    text = text.replace(')', '')
    text = text.replace(',', '')
    text = text.replace("'", '')
    print('##########')
    print(text)
    print(len(text.split()[0]))
    if (len(text.split()[0]) > 20) :
        text="Note*"
        

    # Convert text string to a list of words
    return text.split()

labels =[]
values =[]
with open("wikidatafinal.csv", 'r') as infh:
    reader = csv.reader(infh)
    counter= 0
    for row in reader:
        if counter < 20:
            #print(row)
            labels0 = row[0].split()[0]
            value0  = row[1].split()
            #print(labels0)
            #print(value0)
            item1 = process_text(labels0)
            item2 = process_text(value0[0])
            #print(item1)
            #print(item2)
            labels.append(item1[0]) 
            values.append(int(item2[0])) 
            counter += 1 
print(labels)
print(values)




height = (values)
bars = (labels)

y_pos = np.arange(len(bars))
 
# Create bars and choose color
plt.bar(y_pos, height, color = (0.4,0.3,0.5))

# Add title and axis names
plt.title('Top Twenty Most Frequent Wikidata Revisions ' +'\n' + '15th March 2019 to 1st June 2019', fontsize=20)
plt.xlabel('Wikidata Page Name')
plt.ylabel('Wikidata Revision Frequency')
 
# Limits for the Y axis
plt.ylim(0,1200)
plt.figtext(.65, .65, 'Note* : The page title wikidata labelled Note * is'
                       +'\n' + '"transcriptionfactorsinlightandcircadianclocks'
                        +'\n' + 'ignalingnetworksrevealedbygenomewidemappingof'
                         +'\n' + 'directtargetsforneurosporawhitecollarcomplex"')
# Create names
plt.xticks(y_pos, bars, rotation=70)
#plt.xlabel('my x label', size = 20)
#plt.xlabel('my x label', size = 20)

plt.xticks(size = 12)
#plt.yticks(size = 50)
plt.tight_layout()
# Show graphic
plt.show()


