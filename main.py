import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

df = pd.read_csv('epa-sea-level.csv')

plt.figure(figsize=(12, 6))
plt.plot()
# plt.title('Rise in Sea Level')
plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])


res = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
x = range(df['Year'].min(), 2051)
y = pd.DataFrame(res.slope*x+res.intercept)
plt.plot(x, y, 'g-', label='')


df = df.loc[(df['Year'] >= 2000)]

res1 = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
x = range(df['Year'].min(), 2051)
y = pd.DataFrame(res1.slope*x+res1.intercept)
print(y)
plt.plot(x, y, 'r-', label='')

plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.savefig('sea_level_plot.png')
print(plt.gca())
print(plt.gcf())