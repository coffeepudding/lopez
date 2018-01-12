#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template #追加
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)

@app.route('/')
def hello():
    name = "Hoge"
    #return name
    return render_template('hello.html', title='入退室管理アプリ', name=name) #変更

@app.route('/testpost')
def webhook():
    print request.headers
    print "body: %s" % request.data
    return request.data

## おまじない
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
