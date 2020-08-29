from flask import Flask
from scrape import run as scrape_runner
import pandas as pd
import os

BASEDIR = os.path.dirname(os.path.abspath(__file__))
dataset = os.path.join(BASEDIR, 'data.csv')

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return ' '

@app.route('/scraper', methods=['POST'])
def scraper_view():
    scrape_runner()
    return 'Done'

# app=FastAPI()

@app.route('/phxpolice', methods=['GET'])
def read_data():
    df = pd.read_csv(dataset)
    return df.to_dict("index")
