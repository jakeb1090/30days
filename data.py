import pandas as pd
import requests
import os

file_path = os.path.abspath(__file__)
DATADIR = os.path.dirname(file_path)
filename = os.path.join('dataset.csv', DATADIR)

url = 'https://www.phoenixopendata.com/dataset/cc08aace-9ca9-467f-b6c1-f0879ab1a358/resource/0ce3411a-2fc6-4302-a33f-167f68608a20/download/crimestat.csv'
def clean_data(url):
    df = pd.read_csv(url, low_memory=False, parse_dates=True, nrows=10000)
    df = df.dropna()
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(' ', '_')
    df.occurred_on = df.occurred_on.fillna('')
    df.premise_type = df.premise_type.fillna('')
    df.occurred_on = pd.to_datetime(df.occurred_on)
    df = df.drop(['occurred_to'], axis=1)
    df['100_block_addr'] = df['100_block_addr'].apply(lambda x: x.replace('XX', '00'))
    df['year'] = (df.occurred_on.dt.year).astype(int)
    df['month'] = (df.occurred_on.dt.month).astype(int)
    df['day'] = (df.occurred_on.dt.day).astype(int)
    df['hour'] = (df.occurred_on.dt.hour).astype(int)
    df['day_name'] = df.occurred_on.dt.day_name()
    return df


def write_csv(url):
    df = clean_data(url)
    df.to_csv(filename, index=False)
    return True

