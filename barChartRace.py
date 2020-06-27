import matplotlib.pyplot as plt

from dataCleaning import *
from constants import *

rawdf = getDataFrame(PATHS)
s = rawdf.loc['2020-06-21']
print(s)

fig, ax = plt.subplots(figsize=(4, 2.5), dpi=144)
colors = plt.cm.Dark2(range(6))

print('index', s.index)
y = s.index
print('VALUES', s.values)
width = s.values

print('y', y)
print('width', width)

ax.barh(y=y, width=width, color=colors)

plt.show() 