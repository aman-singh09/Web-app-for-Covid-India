from flask import Flask
import os
from bar import df
from flask import render_template, redirect, request, session, url_for, Response
import pandas as pd
import lxml
import seaborn as sns
import requests
from bs4 import BeautifulSoup, Comment
from io import BytesIO
import base64
import geopandas as gpd

PEOPLE_FOLDER = os.path.join('static')


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER


def table_rep():
    result = requests.get(
        "https://api.apify.com/v2/key-value-stores/toDWvRj1JpTXiM8FF/records/LATEST?disableRedirect=true")
    content = result.json()
    return content


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/state_count')
def state_count():
    tab = table_rep()
    return render_template('state_count.html', tab=tab)


@app.route('/pie')
def pie():
    return render_template('pie.html')


@app.route('/maps')
def maps():
    return render_template('maps.html')


if __name__ == "__main__":
    app.run(debug=True)
