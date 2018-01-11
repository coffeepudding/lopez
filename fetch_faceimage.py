#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Webカメラで常時映像を取り続ける
顔と識別されたら画像を取得する
face/に顔だけ（モデル構築用）
"""
import cv2
import os
from time import sleep
import copy


def main():
    # 検出器もろもろ
    filepath ='/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml'
    face_cascade = cv2.CascadeClassifier(filepath)
    # カメラセット
    capture = cv2.VideoCapture(0)
    # 画像サイズの指定
    ret = capture.set(3, 480)
    ret = capture.set(4, 320)

    pic_i = 0
    while True:
        ret, image = capture.read() # 画像を取得する作業
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face = face_cascade.detectMultiScale(gray_image, scaleFactor=1.3, minNeighbors=2, minSize=(30, 30))

        if len(face) > 0:
            for rect in face:
                # 学習機で使用する顔写真
                face_image = copy.deepcopy(gray_image[rect[1]:rect[1]+rect[3],rect[0]:rect[0]+rect[2]])
                # 顔写真の保存先
                picture_path = "{}/{}.jpg".format(FACEDIR, pic_i)
                # 顔写真の保存
                cv2.imwrite(picture_path, face_image)
                pic_i += 1
                sleep(1)


if __name__ == "__main__":
    # 対象ユーザー名を指定する
    human_name = ""
    FACEDIR = "{}/face/{}".format(os.getcwd(), human_name)
    if not os.path.exists(FACEDIR):
        os.makedirs(FACEDIR)

    main()