#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
from PIL import Image
import sys
import os
from time import sleep
import copy
from datetime import datetime
import numpy as np
import sqlite3

def monitor():
    # カメラセット
    capture = cv2.VideoCapture(0)
    # 画像サイズの指定
    ret = capture.set(3, 480)
    ret = capture.set(4, 320)
    while True:
        ret, image = capture.read() # 画像を取得する作業
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face = face_cascade.detectMultiScale(gray_image, scaleFactor=1.3, minNeighbors=2, minSize=(30, 30))

        if len(face) > 0:
            rect = face[0]
            # 学習機で使用する顔写真
            face_image = copy.deepcopy(gray_image[rect[1]:rect[1]+rect[3],rect[0]:rect[0]+rect[2]])
            # 顔写真の保存先
            # 写真の命名規則: 2018/01/12-12:36:57
            picture_path = "{}/faces/{}.jpg".format(os.getcwd(), datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            # 顔写真の保存
            face_image = cv2.resize(face_image, (200, 200), interpolation=cv2.INTER_LINEAR)
            cv2.imwrite(picture_path, face_image)
            # 顔を識別する
            # 画像をnumpyの形式に変更する
            test_image = np.array(face_image, 'uint8')
            label, confidence = recognizer.predict(test_image)
            break
    capture.release()
    return human[label], picture_path, confidence


def store_data(username, timestamp):
    conn = sqlite3.connect("../monitoring.db")
    conn.text_factory = str
    cur = conn.cursor()

    # 既に入室しているかどうかを確認する
    status = ""
    sql = "SELECT count(*) from app WHERE username = {} AND timestamp LIKE '{}%' ORDER BY timstamp asc".format(username, timestamp.split(' '[0]))
    for row in c.execute(sql):
        count = row[0]
    if count == 0:
        status = "入室"
    elif count % 2 == 1:
        status == "入室"
    elif count % 2 == 0:
        status == "退室"

    sql = "INSERT INTO app (username, timestamp, status) values( ?, ?, ? )"
    user = (str(username), str(timestamp), str(status))
    cur.execute(sql, user)
    conn.commit()
    conn.close()


def main():
    while True:
        label, filename, confidence  = monitor()
        print("氏名: {}, ファイル名: {}, 確信度: {}".format(label, filename, confidence))
        filename = filename.split("/")[-1].replace(".jpg", "")
        store_data(label, filename)
        sleep(5)


if __name__ == "__main__":
    # 分類器を読み込む
    # EigenFace
    #recognizer = cv2.face.EigenFaceRecognizer_create()
    # FisherFace
    recognizer = cv2.face.FisherFaceRecognizer_create()
    # LBPH
    #recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('human_model.xml')
    # human_model
    human = {0: "西開地", 1: "平野", 2: "亘理"}
    # 検出器もろもろ
    filepath ='/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml'
    face_cascade = cv2.CascadeClassifier(filepath)

    main()
