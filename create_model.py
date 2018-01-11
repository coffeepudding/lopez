#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2, os
import numpy as np
from PIL import Image
import time
import copy
import glob
import pickle

# 指定されたpath内の画像を取得
def get_images_and_labels(path):
    # 人の種類
    human = {"nishikaichi": 0, "hirano": 1, "watari": 2}
    # 画像を格納する配列
    images = []
    # ラベルを格納する配列
    labels = []
    for f in path:
        # グレースケールで画像を読み込む
        image_pil = Image.open(image_path).convert('L')
        # NumPyの配列に格納
        image = np.array(image_pil, 'uint8')
        # 画像を配列に格納
        images.append(image)
        # ファイル名からラベルを取得
        labels.append(human[f.split("/")[-2]])
   return images, labels


def main():
    # トレーニング画像（わたりのみ対応）
    train_path = './watariface'

    # テスト画像（デバッグ）
    test_path = './test'

    facepath = "{}/face/*/*.jpg".format(os.getcwd())
    files = []
    files = glob.glob(facepath)

    # # 顔認識器の構築 for OpenCV 2
    # # ※ OpenCV3ではFaceRecognizerはcv2.faceのモジュールになります
    # # EigenFace
    # #recognizer = cv2.face.EigenFaceRecognizer_create()
    # # FisherFace
    # #recognizer = cv2.face.FisherFaceRecognizer_create()
    # # LBPH
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    # トレーニング画像を取得
    images, labels = get_images_and_labels(facepath)

    # トレーニング実施
    recognizer.train(images, np.array(labels))

    # 学習済みモデルの保存
    with open('human_model.pickle', mode='wb') as f:
        pickle.dump(recognizer, f)


if __name__ == "__main__":
    main()
