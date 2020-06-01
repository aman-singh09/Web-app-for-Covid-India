from flask import Flask
import os
from bar import plt
from flask import render_template, redirect, request, session,url_for,Response
import pandas as pd
import lxml
import seaborn as sns
import requests
from bs4 import BeautifulSoup
from io import BytesIO
import base64
import geopandas as gpd

PEOPLE_FOLDER = os.path.join('static')


app =Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

def table_rep():
    url = 'https://www.mohfw.gov.in/'
    web_content = requests.get(url).content
    soup = BeautifulSoup(web_content, "lxml")

    all_rows = soup.find_all('tr')
    return all_rows


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/state_count')
def state_count():
    tab=table_rep()
    return render_template('state_count.html',tab=tab)

@app.route('/pie')
def pie():
    return render_template('pie.html')

@app.route('/bar')
def bar(): 
    plt.plot()
    plt.savefig('./static/image.png')
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    result = figdata_png
    result = str(figdata_png)[2:-1]
    return render_template('bar.html',result=result)

@app.route('/maps')
def maps():
    return render_template('maps.html')


if __name__ == "__main__":
    app.run(debug=True)
