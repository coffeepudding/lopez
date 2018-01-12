#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
import sqlite3 #追加
import sys
from codes import test

reload(sys)
sys.setdefaultencoding('utf-8')
dbname = 'monitoring.db'

def fetch_data():
    res = []
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    sql = "SELECT * FROM app ORDER BY timestamp desc"
    for row in c.execute(sql):
        res.append({"username": row[0], "timestamp": row[1], "inout": row[2]})
    conn.close()
    return res

app = Flask(__name__)

@app.route('/')
def hello():
    name = "Hoge"
    db = fetch_data()
    cumtime = {"0": test.calc_time("西開地"), "1": test.calc_time("平野"), "2": test.calc_time("亘理")}
    print(cumtime)
    return render_template('hello.html', title='入退室管理アプリ', data_list=db, time = cumtime, enumerate=enumerate) #変更

@app.route('/testpost', methods=["GET","POST"])
def testpost():
    return render_template('hello.html', title='入退室管理アプリ',aaa=hoge) #変更

## おまじない
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
