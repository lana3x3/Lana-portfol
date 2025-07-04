# -*- coding: utf-8 -*-
"""Data_Visualization_Info (1).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Lg8ZMkcWCgeMSIz4EEefsMZp2bn1xlsJ
"""

import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[10,15,7,2,18]

#create a line plot
plt.plot(x,y, marker='o', linestyle='-',color='b',label='Line')

#Add titles and labels
plt.title('Basic line plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)

plt.plot()

import numpy as np
category=['A','B','C','D','E']
values=[10,25,15,20,30]

#create a bar chart
plt.bar(category,values, color='blue',alpha=0.7)

plt.title('Bar Chart Example')
plt.xlabel('Category')
plt.ylabel('Values')

#Display the plot
plt.show()

data=np.random.randn(1000)
plt.hist(data, bins=30, color='green',edgecolor='black',alpha=0.7)

plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.show()

import seaborn as sns
tips=sns.load_dataset('tips')

#Lineplot
sns.lineplot(x='total_bill',y='tip',data=tips)
plt.title('Lineplot')
plt.show()

#BarPlot
sns.barplot(x='day',y='total_bill',data=tips, palette='viridis')
plt.title('Bar Plot')
plt.show()

#Histogram
sns.histplot(tips['total_bill'],kde=True, bins=30, color='blue')
plt.title('Histogram plot')
plt.show()

#Scatter Plot
sns.scatterplot(x='total_bill', y='tip', data=tips, hue='day',style='time',palette='coolwarm')
plt.title('Scatter plot')
plt.show()

#Pairplot
sns.pairplot(tips, hue='sex',palette='husl')
plt.show()

