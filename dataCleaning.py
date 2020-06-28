import pandas as pd
from datetime import datetime
from datetime import date
from constants import *

def getDates():
    times = pd.date_range(FIRST_DATE, periods=DAYS, freq='D')
    return times

def getStates():
    df = pd.read_csv(PATHS[0])
    states_list = df['Province_State'].values.tolist()
    return states_list

def getConfirmedCases(path):
    df = pd.read_csv(path)
    return df[['Confirmed']]

def getRowIndices():
    rename_dict = {}
    # Create dictionary for renaming row indices
    for i in range(len(PATHS)):
        path = PATHS[i]
        date_string = path[5:15]
        datetime_obj = datetime.strptime(date_string, '%m-%d-%Y')
        rename_dict[i] = datetime_obj
    return rename_dict

def getDataFrame(paths):
    frame = pd.DataFrame()
    states = getStates()

    for path in paths:
        cases = getConfirmedCases(path)
        frame = frame.append(cases.T, ignore_index=True)

    frame.columns = states
    frame.rename(index=getRowIndices(), inplace=True)
    return frame
    
def beautify_axes(ax):
    ax.set_facecolor('.8')
    ax.tick_params(labelsize=8, length=0)
    ax.grid(True, axis='x', color='white')
    ax.set_axisbelow(True)
    [spine.set_visible(False) for spine in ax.spines.values()]  

if __name__ == '__main__':
    print(getDataFrame(PATHS))

# Todo:
# Add date as the row index
# Continue into https://medium.com/dunder-data/create-a-bar-chart-race-animation-in-python-with-matplotlib-477ed1590096
# Flag for fetching data dynamically
# Generate date dynamically