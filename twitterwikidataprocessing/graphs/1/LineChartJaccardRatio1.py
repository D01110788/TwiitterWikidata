# libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


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

item1list =[]
item2list =[]
#with open("listjacartadistance1.csv", 'r') as infh:
with open("listjacartadistance1A.csv", 'r') as infh:
    reader = csv.reader(infh)
    counter= 0
    for row in reader:
            print(row)
            item1 = row[0].split(',')[0]
            itemPre2  = row[3].split()
            itemPre3  = row[2].split()
            item2 = process_text(itemPre2[0])
            item3 = process_text(itemPre3[0])
            print(item2)
            print(item3)
            for i in item2:
                item1list.append(float(i))
            for j in item3:
                item2list.append(float(j))

#Similarity
print(item1list)
seta = set(item1list)
b = [item1list.count(el) for el in seta]
a = list(seta) #Only if you really want it.

plt.plot(a, b, "go")
plt.title("Jaccard's Similarity Scatter Plot for .01 Percent of Data \n and 1-Grams Twitter Hashtags")
plt.xlabel("Jaccard's Similarity")
plt.ylabel('Frequency')
plt.show()


#Distance
print(item2list)
seta = set(item2list)
b = [item2list.count(el) for el in seta]
a = list(seta) #Only if you really want it.

plt.plot(a, b, "go")
plt.title("Jaccard's Distance Scatter Plot for .01 Percent of Data \n and 1-Grams Twitter Hashtags")
plt.xlabel("Jaccard's Distance")
plt.ylabel('Frequency')
plt.show()








