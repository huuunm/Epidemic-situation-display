import json
import os
import time
from datetime import datetime

from flask import Flask, app, render_template, request

from crawler import Crawler

BASE_DIR = os.path.dirname(__file__)
app = Flask(__name__,
            template_folder=os.path.join(BASE_DIR, "templates"),
            static_folder=os.path.join(BASE_DIR, "static"),
            static_url_path="/static")

app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/getmap', methods=['GET', 'POST'])
def getmap():
    return render_template('getmap.html')


@app.route('/getRTBaiduData', methods=['GET', 'POST'])
def getRTBaiduData():
    return str(Crawler().getBaiduRTData()).replace(
        '\'', '"').replace('"hasTongji": True',
                           '"hasTongji": "True"').replace("\\", "\\\\")


@app.route('/ncov', methods=['GET', 'POST'])
def ncov():
    dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('ncov.html', date=dt, area='全国')


if __name__ == '__main__':
    app.run()
