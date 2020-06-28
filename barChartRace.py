import pandas as pd
import matplotlib.pyplot as plt
from dataCleaning import *
from constants import *
from prepareData import *

dataframe = getDataFrame(PATHS)
s = dataframe.loc['2020-06-21']

dataframe.index = pd.to_datetime(dataframe.index)

#################################
# Smoothly transition by interpolating data
#################################

# Create dataframe with all the data
df2 = dataframe.loc[DATES[0]:DATES[-1]]

df_expanded, df_rank_expanded = prepare_data(df2)

# Create single chart
# fig, ax = plt.subplots(figsize=(4, 2.5), dpi=144)
colors = plt.cm.Dark2(range(50))

# Get data for chart
states_array = s.index
number_of_cases = s.values

# Add data to chart
# ax.barh(y=states_array, width=number_of_cases, color=colors)
# beautify_axes(ax)

# Plot each step of the transition
fig, ax_array = plt.subplots(nrows=1, ncols=6, figsize=(12,2), dpi=144, tight_layout=True)
labels = df_expanded.columns
for i, ax in enumerate(ax_array.flatten()):
    y = df_rank_expanded.iloc[i]
    width = df_expanded.iloc[i]
    ax.barh(y=y, width=width, color=colors, tick_label=labels)
    beautify_axes(ax)

ax_array[0].set_title('one')
ax_array[-1].set_title('two')

# Create three charts
# fig, ax_array = plt.subplots(nrows=1, ncols=3, figsize=(7, 2.5), dpi=144, tight_layout=True)
# for ax, date in zip(ax_array, DATES):
#     ranked_states = dataframe.loc[date]
#     y = dataframe.loc[date].rank(method='first').values
#     ax.barh(y=y, width=ranked_states.values, color=colors, tick_label=ranked_states.index)
#     ax.set_title(date, fontsize='smaller')
#     beautify_axes(ax)

# Render chart
plt.show() 