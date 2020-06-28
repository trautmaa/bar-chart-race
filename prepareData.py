import pandas as pd
import matplotlib.pyplot as plt
from dataCleaning import *
from constants import *

def prepare_data(df, steps=5):
    # Use numerical indices rather than date
    df = df.reset_index()

    # Multiply each index number by number of steps
    df.index = df.index * steps

    # Add empty rows for each intermediary step
    last_index = df.index[-1] + 1
    df_expanded = df.reindex(range(last_index))

    # Fill NaN with last known date
    df_expanded['index'] = df_expanded['index'].fillna(method='ffill')

    # Reset index to the index column, which holds the date
    df_expanded = df_expanded.set_index('index')

    # Create new dataframe to hold state rank
    df_rank_expanded = df_expanded.rank(axis=1, method='first')

    # Interpolate those intermediary values for df_expanded
    df_expanded = df_expanded.interpolate()

    # Interpolate rankings
    df_rank_expanded = df_rank_expanded.interpolate(method ='linear', limit_direction ='forward')

    return df_expanded, df_rank_expanded
