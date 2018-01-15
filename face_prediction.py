#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
実行環境: python2
実行方法: python fetch_prediction.py <対象人物>
Webカメラで常時映像を取り続ける
顔と識別されたら画像を取得する
face/に顔だけ（モデル構築用）
"""
import cv2
import numpy as np
from PIL import Image

# 顔認識器の構築 for OpenCV 2
# ※ OpenCV3ではFaceRecognizerはcv2.faceのモジュールになります
# EigenFace
#recognizer = cv2.face.EigenFaceRecognizer_create()
# FisherFace
recognizer = cv2.face.FisherFaceRecognizer_create()
# LBPH
#recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('human_model.xml')

# テスト画像を取得
test_image = Image.open('test.jpg').convert('L')
# NumPyの配列に格納
image = np.array(test_image, 'uint8')

# 予測
label, confidence = recognizer.predict(image)
print("ラベル:{},確信度{}".format(label,confidence))
