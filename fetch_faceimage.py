#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
実行環境: python2
実行方法: python fetch_faceimage.py <対象人物>
Webカメラで常時映像を取り続ける
顔と識別されたら画像を取得する
face/に顔だけ（モデル構築用）
"""
import cv2
import sys
import os
from time import sleep
import copy


def main():
    # 保存先ディレクトリの確認 && 保存
    args = sys.argv
    # 対象ユーザー名をコマンドライン引数から取得
    human_name = args[1]
    FACEDIR = "{}/face/{}".format(os.getcwd(), human_name)
    if not os.path.exists(FACEDIR):
        os.makedirs(FACEDIR)

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
                print("人を検知しました: {}回目".fortmat(pic_i))
                # 学習機で使用する顔写真
                face_image = copy.deepcopy(gray_image[rect[1]:rect[1]+rect[3],rect[0]:rect[0]+rect[2]])
                # 顔写真の保存先
                picture_path = "{}/{}.jpg".format(FACEDIR, pic_i)
                # 顔写真の保存
                cv2.imwrite(picture_path, face_image)
                pic_i += 1
                sleep(1)


if __name__ == "__main__":
    main()