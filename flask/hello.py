#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template #追加

app = Flask(__name__)

@app.route('/')
def hello():
    name = "Hoge"
    #return name
    return render_template('hello.html', title='入退室管理アプリ', name=name) #変更

## おまじない
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
