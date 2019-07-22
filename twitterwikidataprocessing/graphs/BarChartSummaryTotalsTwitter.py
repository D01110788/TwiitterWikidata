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
height = [52633, 145133, 132300, 128791]
bars = ('1-grams', '2-grams', '3-grams', '4-grams')
y_pos = np.arange(len(bars))
 
# Create bars and choose color
plt.bar(y_pos, height, color = (0.5,0.1,0.5,0.6))
 
# Add title and axis names
plt.title('Total Twitter Hashtags Processed Per N-Grams')
plt.ylabel('Total Twitter Hashtags')
 
# Limits for the Y axis
plt.ylim(0,150000)
 
# Create names
plt.xticks(y_pos, bars)
 
plt.tight_layout()
# Show graphic
plt.show()
