#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, sqlite3 #追加
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
dbname = 'monitoring.db'

def fetch_data():
    res = []
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    sql = "SELECT * FROM app ORDER BY timestamp desc"
    for row in c.execute(sql):
        res.append(["username": row[0], "timestamp": row[1]])
    conn.close()
    return res

app = Flask(__name__)

@app.route('/')
def hello():
    name = "Hoge"
    #return name
    return render_template('hello.html', title='入退室管理アプリ', name=name) #変更

@app.route('/testpost', methods=["GET","POST"])
def testpost():
    return render_template('hello.html', title='入退室管理アプリ',aaa=hoge) #変更

## おまじない
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
