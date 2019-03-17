# run.py

from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import pandas as pd
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import csv

APP = Flask(
    __name__, static_folder="../dist/static", template_folder="../dist"
)
cors = CORS(APP, resources={r"*": {"origins": "*"}})

fileList = []

@APP.route("/")
def home():
    return render_template('index.html')

@APP.route("/test", methods=['GET', 'POST'])
def test():
    response ={
        'res': 'caonima'
    }
    return jsonify(response)

@APP.route("/upload", methods=['GET', 'POST'])
def upload():
    global fileList
    f = request.files['file']
    # csv_file = csv.reader(f, "rb")
    # print(csv_file)

    csv_file = csv.reader(f.filename)
    f.save(str(f.filename))
    df = pd.read_csv(f.filename)
    print(df.values)
    current = {
        'time': df['date'][0] + '- ' + df['date'][df.shape[0] - 1],
        'type': 'csv',
        'source': '线上渠道',
        'area': '中国',
        'class': df['关键词'][0],
        'tableData': df.values.tolist()
    }
    fileList.append(current)
    response = {
        'res': fileList,
        
    }
    # with open(f.filename,mode='r',encoding='utf-8',newline='') as f:
    #     #此处读取到的数据是将每行数据当做列表返回的
    #     reader = csv.reader(f)
    #     for row in reader:
    #         #此时输出的是一行行的列表
    #         # print(row)
    #         print(row)

    return jsonify(response)

@APP.route("/clear", methods=['GET', 'POST'])
def clearList():
    global fileList
    fileList = []
    response ={
        'code': 200
    }
    return jsonify(response)

@APP.route("/getlist", methods=['GET', 'POST'])
def getlist():
    response ={
        'res': fileList
    }
    return jsonify(response)

if __name__ == '__main__':
    APP.run(debug=True, host="0.0.0.0")