# !pip install brewer2mpl
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')
import random
import csv


# libraries
import numpy as np
import matplotlib.pyplot as plt
 
# Fake dataset

height = [1867281, 270135]
bars = ('Collected', 'Processed')
y_pos = np.arange(len(bars))
 
# Create bars and choose color
plt.bar(y_pos, height, color = (0.5,0.1,0.5,0.6))
 
# Add title and axis names
plt.title('Total Unique Wikidata Pages (Collected and Processed)')

# Create bars and choose color
plt.bar(y_pos, height, color = (0.2,0.1,0.5,0.8))
 
# Add title and axis names

plt.ylabel('Total Wikidata Pages')
 
# Limits for the Y axis
plt.ylim(0,2000000)
 
# Create names
plt.xticks(y_pos, bars)
 
plt.tight_layout()
# Show graphic
plt.show()


######
#####   THIS WAS FRO FREQUENCY HASHTAGS BUT NO TIME
#####

# Add title and axis names
plt.title('Total Wikidata Pages and and Revisions '  +'\n' + '15th March 2019 to 1st June 2019')
plt.xlabel('Hashtag Name')
plt.ylabel('Twitter Hashtag Frequency')
 
# Limits for the Y axis
plt.ylim(0,50000)
 
# Create names
plt.xticks(y_pos, bars, rotation=70)

# Show graphic
plt.show()

