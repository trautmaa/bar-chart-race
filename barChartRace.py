import matplotlib.pyplot as plt
from dataCleaning import *
from constants import *

rawdf = getDataFrame(PATHS)
s = rawdf.loc['2020-06-21']

# Create single chart
# fig, ax = plt.subplots(figsize=(4, 2.5), dpi=144)
colors = plt.cm.Dark2(range(6))


# Get data for chart
states_array = s.index
number_of_cases = s.values

# Add data to chart
# ax.barh(y=states_array, width=number_of_cases, color=colors)
# beautify_axes(ax)

# Create three charts
fig, ax_array = plt.subplots(nrows=1, ncols=3, figsize=(7, 2.5), dpi=144, tight_layout=True)
dates = ['06-21-2020', '06-22-2020', '06-23-2020']
for ax, date in zip(ax_array, dates):
    s = rawdf.loc[date].sort_values()
    ax.barh(y=s.index, width=s.values, color=colors)
    ax.set_title(date, fontsize='smaller')
    beautify_axes(ax)

# Render chart
plt.show() 