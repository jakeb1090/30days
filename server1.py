from flask import Flask
from scrape import run as scrape_runner
import pandas as pd
import os
import data

BASEDIR = os.path.dirname(os.path.abspath(__file__))
dataset = os.path.join(BASEDIR, 'dataset.csv')

url = 'https://www.phoenixopendata.com/dataset/cc08aace-9ca9-467f-b6c1-f0879ab1a358/resource/0ce3411a-2fc6-4302-a33f-167f68608a20/download/crimestat.csv'


app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Index '

@app.route('/scraper', methods=['POST'])
def scraper_view():
    scrape_runner()
    return 'Done'

# app=FastAPI()

@app.route('/phxpolice', methods=['GET'])
def disp_data(url=url):
    df = data.write_csv(url)
    df = pd.read_csv(dataset)
    return df.to_dict("index")


