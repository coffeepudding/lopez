#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
from PIL import Image
import sys
import os
from time import sleep
import copy
from datetime import datetime

def main():
    # 分類器を読み込む
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('human_model.xml')

    # 検出器もろもろ
    filepath ='/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml'
    face_cascade = cv2.CascadeClassifier(filepath)
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
            for rect in face:
                # 学習機で使用する顔写真
                face_image = copy.deepcopy(gray_image[rect[1]:rect[1]+rect[3],rect[0]:rect[0]+rect[2]])
                # 顔写真の保存先
                # 写真の命名規則: 2018/01/12-12:36:57
                picture_path = "{}/faces/{}.jpg".format(os.getcwd(), datetime.now().strftime("%Y/%m/%d-%H:%M:%S"))
                # 顔写真の保存
                face_image = cv2.resize(face_image, (200, 200), interpolation=cv2.INTER_LINEAR)
                cv2.imwrite(picture_path, face_image)
                # 顔写真をモデルにツッコミ判定を行う
                test_image = Image.open(picture_path).convert('L')
                label, confidence = recognizer.predict(test_image)
                print("ラベル:{},確信度{}".format(label,confidence))
                sleep(3)


if __name__ == "__main__":
    main()