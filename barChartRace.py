import pandas as pd
import matplotlib.pyplot as plt
from dataCleaning import *
from constants import *
from prepareData import *

dataframe = getDataFrame(PATHS)
s = dataframe.loc['2020-06-21']

dataframe.index = pd.to_datetime(dataframe.index)

# Create dataframe with all the data
df2 = dataframe.loc[DATES[0]:DATES[-1]]

# Create expanded dataframes with interpolated data for
# animating the transitions
df_expanded, df_rank_expanded = prepare_data(df2)

colors = plt.cm.Dark2(range(50))

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

# Render chart
plt.show() 