import pandas as pd

def getConfirmedCases(path):
    df = pd.read_csv(path)
    return df[['Province_State', 'Confirmed']]

def common():
    paths = ['data/06-21-2020.csv', 'data/06-22-2020.csv', 'data/06-23-2020.csv']
    frame = pd.DataFrame()

    for path in paths:
        cases = getConfirmedCases(path)
        frame = frame.append(cases.T, ignore_index=True)

    print(frame)
        

if __name__ == '__main__':
    common() 