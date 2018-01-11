#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2, os
import numpy as np
from PIL import Image
import time
import copy
import glob

# 指定されたpath内の画像を取得
def get_images_and_labels(path):
   # 画像を格納する配列
   images = []
   # ラベルを格納する配列
   labels = []
   # ファイル名を格納する配列
   files = []
   for f in os.listdir(path):
       # 画像のパス
       image_path = os.path.join(path, f)
       #print(f)
       # グレースケールで画像を読み込む
       image_pil = Image.open(image_path).convert('L')
       # NumPyの配列に格納
       image = np.array(image_pil, 'uint8')
       # Haar-like特徴分類器で顔を検知
       faces = face_cascade.detectMultiScale(image)
       # 検出した顔画像の処理
       for (x, y, w, h) in faces:
           # 顔を 200x200 サイズにリサイズ
           roi = cv2.resize(image[y: y + h, x: x + w], (200, 200), interpolation=cv2.INTER_LINEAR)
           # 画像を配列に格納
           images.append(roi)
           # ファイル名からラベルを取得
           labels.append(0)
           # ファイル名を配列に格納
           files.append(f)

   return images, labels, files


def main():
    # トレーニング画像（わたりのみ対応）
    train_path = './watariface'

    # テスト画像（デバッグ）
    test_path = './test'

    facepath = "{}/face/*/*.jpg".format(os.getcwd())
    files = []
    files = glob.glob(facepath)
    print(files)

    # # 検出器もろもろ
    # filepath ='/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml'
    # #filepath ='/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml'
    # face_cascade = cv2.CascadeClassifier(filepath)

    # # 顔認識器の構築 for OpenCV 2
    # # ※ OpenCV3ではFaceRecognizerはcv2.faceのモジュールになります
    # # EigenFace
    # #recognizer = cv2.face.EigenFaceRecognizer_create()
    # # FisherFace
    # #recognizer = cv2.face.FisherFaceRecognizer_create()
    # # LBPH
    # recognizer = cv2.face.LBPHFaceRecognizer_create()

    # # トレーニング画像を取得
    # images, labels, files = get_images_and_labels(facepath)

    # # トレーニング実施
    # recognizer.train(images, np.array(labels))

    # # テスト画像を取得
    # #test_images, test_labels, test_files = get_images_and_labels(test_path)


if __name__ == "__main__":
    main()
