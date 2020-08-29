
import data
import os
import pandas as pd
from fastapi import FastAPI
from flask import Flask

BASEDIR = os.path.dirname(os.path.abspath(__file__))
dataset = os.path.join(BASEDIR, 'data.csv')


app=FastAPI()

@app.get("/")
def hello_world():
    return {'hello':'world'}

@app.get("/phxpolice")
def read_data():
    df = pd.read_csv(dataset)
    return df.to_dict()
