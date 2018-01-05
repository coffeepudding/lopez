#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2, os
import numpy as np
from PIL import Image
import time

# トレーニング画像（わたりのみ対応）
train_path = './watariface'

# テスト画像（デバッグ）
test_path = './test'

# 検出器もろもろ
filepath ='/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml'
#filepath ='/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml'
face_cascade = cv2.CascadeClassifier(filepath)

# 顔認識器の構築 for OpenCV 2
# ※ OpenCV3ではFaceRecognizerはcv2.faceのモジュールになります
# EigenFace
#recognizer = cv2.createEigenFaceRecognizer()
# FisherFace
#recognizer = cv2.createFisherFaceRecognizer()
# LBPH
recognizer = cv2.face.LBPHFaceRecognizer_create()


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
       # グレースケールで画像を読み込む
       image_pil = Image.open(image_path).convert('L')
       # NumPyの配列に格納
       image = np.array(image_pil, 'uint8')
       # Haar-like特徴分類器で顔を検知
       faces = faceCascade.detectMultiScale(image)
       # 検出した顔画像の処理
       for (x, y, w, h) in faces:
           # 顔を 200x200 サイズにリサイズ
           roi = cv2.resize(image[y: y + h, x: x + w], (200, 200), interpolation=cv2.INTER_LINEAR)
           # 画像を配列に格納
           images.append(roi)
           # ファイル名からラベルを取得
           labels.append(int(f[7:9]))
           # ファイル名を配列に格納
           files.append(f)

   return images, labels, files


capture = cv2.VideoCapture(0) # カメラセット
# 画像サイズの指定
ret = capture.set(3, 480)
ret = capture.set(4, 320)

# トレーニング画像を取得
#images, labels, files = get_images_and_labels(train_path)

# トレーニング実施
#recognizer.train(images, np.array(labels))

# テスト画像を取得
#test_images, test_labels, test_files = get_images_and_labels(test_path)


i = 0
while True:
    start = time.clock() # 開始時刻
    ret, image = capture.read() # 画像を取得する作業
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray_image, scaleFactor=1.3, minNeighbors=2, minSize=(30, 30))

    if len(face) > 0:
        for rect in face:
            cv2.rectangle(image, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), (0, 0,255), thickness=2)

    get_image_time = int((time.clock()-start)*1000) # 処理時間計測
    # 1フレーム取得するのにかかった時間を表示
    cv2.putText( image, str(get_image_time)+"ms", (10,10), 1, 1, (0,255,0))

   # テスト画像に対して予測実施
   #label, confidence = recognizer.predict()

    cv2.imshow("Camera Test",image)
    # キーが押されたら保存・終了
    if cv2.waitKey(10) == 32: # 32:[Space]
        cv2.imwrite(str(i)+".jpg",image)
        i+=1
        print("Save Image..."+str(i)+".jpg")
    elif cv2.waitKey(10) == 27: # 27:Esc
        capture.release()
        cv2.destroyAllWindows()
        break
