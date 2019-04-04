# run.py

from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import pandas as pd
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from test import HMM, triangle, triangle2
import csv
import random
import datetime

APP = Flask(
    __name__, static_folder="../dist/static", template_folder="../dist"
)
cors = CORS(APP, resources={r"*": {"origins": "*"}})

fileList = []
predictList = []
planList = []


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
    # print(df.values)
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

@APP.route("/upload1", methods=['GET', 'POST'])
def upload1():
    response = {
        'code': 200
    }
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

@APP.route("/predict", methods=['GET', 'POST'])
def predict():
    global predictList
    #print(request.args.get('index'))
    #print(fileList[int(request.args.get('index'))])
    a = fileList[int(request.args.get('index'))]
    print('123')
    print(a['tableData'][0][0])
    print('456')
    b = []
    for i in a['tableData']:
        # print(i)
        b.append(i[6])
    tri_x, tri_y = triangle(30, b)
    # x, y = triangle2(39)
    hmm = HMM(5, 400)
    hmm.train(tri_y)
    y = hmm.generate(365)
    res = []
    begin = datetime.date(2019,1,11)
    delta = datetime.timedelta(days = 1)
    for i in range(len(y)):
        current = {
            'time': begin.strftime("%Y-%m-%d"),
            'sales': y[i] * 100 + random.randint(0, 100)
        }
        begin += delta
        #res.append(y[i] * 100 + random.randint(0, 100))
        res.append(current)
    # print(triangle(20))
    predictData = {
        a['tableData'][0][0]: res,
    }
    predictList.append(predictData)
    print(predictData)
    response = {
        'res': res
    }
    return jsonify(response)

@APP.route("/submitplan", methods=['GET', 'POST'])
def submitplan():
    global planList
    b = {
        'name': request.args.get('name'),
        'heiyumi':request.args.get('heiyumi'),
        'huayumi':request.args.get('huayumi'),
        'tianyumi': request.args.get('tianyumi'),
        'key': request.args.get('key'),
    }
    planList.append(b)
    print(planList)
    response = {
        'code': 200
    }
    return jsonify(response)

@APP.route("/getplan", methods=['GET', 'POST'])
def getplan():
    global planList
    response = {
        'res': planList
    }
    return jsonify(response)


if __name__ == '__main__':
    APP.run(debug=True, host="0.0.0.0")