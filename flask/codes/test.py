#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import datetime

def calc_func(x):
    a, b = x.split(' ')
    year, month, day = [int(v) for v in a.split("-")]
    hour, minute, second = [int(v) for v in b.split(":")]
    return datetime.datetime(year, month, day, hour, minute, second)


def calc_time(username):
    conn = sqlite3.connect("./monitoring.db")
    conn.text_factory = str
    cur = conn.cursor()
    a, b = [], []
    # username = "西開地"
    sql = "SELECT * FROM app WHERE username = '{}' ORDER BY timestamp asc".format(username)
    for row in cur.execute(sql):
        username = row[0]
        timestamp = row[1]
        status = row[2]
        if status == "入室":
            a.append(timestamp)
        else:
            b.append(timestamp)
    time = 0
    for x, y in zip(a, b):
        c = calc_func(x)
        d = calc_func(y)
        time += (d - c).total_seconds()

    hour = int(time // 3600)
    minute = int((time - hour * 3600) // 60)
    second = int((time - hour * 3600 - minute * 60))
    return "{}:{}:{}".format(str(hour).zfill(2), str(minute).zfill(2), str(second).zfill(2))


if __name__ == "__main__":
    main()
