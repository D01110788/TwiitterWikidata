# !pip install brewer2mpl
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')
import random
import csv


def process_text(text): 
    text = text.replace('(', '')
    text = text.replace(')', '')
    text = text.replace(',', '')
    text = text.replace("'", '')
     # Convert text string to a list of words
    return text.split()

labels =[]
values =[]
with open("ngramschartsTHREE.csv", 'r') as infh:
    reader = csv.reader(infh)
    counter= 0
    for row in reader:
        if counter < 20:
            print(row)
            labels0 = row[0].split()[0]
            value0  = row[1].split()
            print(labels0)
            print(value0)
            item1 = process_text(labels0)
            item2 = process_text(value0[0])
            print(item1)
            print(item2)
            labels.append(item1[0]) 
            values.append(int(item2[0])) 
            counter += 1 
print(labels)
print(values)




height = (values)
bars = (labels)
y_pos = np.arange(len(bars))
 
# Create bars and choose color
plt.bar(y_pos, height, color = (0.2,0.4,0.9))

# Add title and axis names
plt.title('Top Twenty Most Frequent Twitter Hashtags with 3-Grams' +'\n' + '15th March 2019 to 1st June 2019', fontsize=20)
plt.xlabel('Hashtag Name')
plt.ylabel('Twitter Hashtag Frequency')
 
# Limits for the Y axis
plt.ylim(0,40000)
 
# Create names
plt.xticks(y_pos, bars, rotation=70)
plt.xticks(size = 12)
#plt.yticks(size = 50)
plt.tight_layout()
# Show graphic
plt.show()

