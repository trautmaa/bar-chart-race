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
    # datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
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
    
if __name__ == '__main__':
    print(getDataFrame(PATHS))

# Todo:
# Add date as the row index
# Continue into https://medium.com/dunder-data/create-a-bar-chart-race-animation-in-python-with-matplotlib-477ed1590096
# Flag for fetching data dynamically
# Generate date dynamically