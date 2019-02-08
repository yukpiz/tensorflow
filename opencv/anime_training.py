# codeing:utf-8

import cv2
import os
import glob
import imghdr

import tensorflow as tf
from tensorflow import keras
from decimal import Decimal

import numpy as np
import matplotlib.pyplot as plt


PROC_PATHS = [
    "data/dst/face/zombi1.mp4/",
    "data/dst/face/zombi2.mp4/",
    "data/dst/face/zombi3.mp4/",
]

IMG_DIR_NAMES = [
    "0_sakura_minamoto",
    "1_saki_nikaido",
    "2_ai_mizuno",
    "3_junko_konno",
    "4_yugiri",
    "5_lily_hoshikawa",
    "6_tae_yamada",
    "7_kotaro_tatsumi",
]

CLASS_NAMES = [
    "Sakura Minamoto",
    "Saki Nikaido",
    "Ai Mizuno",
    "Junko Konno",
    "Yugiri",
    "Lily Hoshikawa",
    "Tae Yamada",
    "Kotaro Tatsumi",
]

FIXED_IMAGE_SIZE = 28


class NotMatchCountError(Exception):
    def __init__(self, message):
        self.message = message


def main(proc_paths, img_dir_names):
    image_bytes = []
    image_labels = []
    image_count = 0
    for proc_path in proc_paths:

        label_index = 0
        for img_dir_name in img_dir_names:

            target = os.path.join(proc_path, img_dir_name)
            for image_path in glob.glob('{}/*.*'.format(target), recursive=False):

                # 画像ファイル以外はスキップ
                if imghdr.what(image_path) is None:
                    continue
                image_count += 1

                image_byte = cv2.imread(image_path, cv2.IMREAD_COLOR)
                image_byte = cv2.resize(
                    image_byte, (FIXED_IMAGE_SIZE, FIXED_IMAGE_SIZE))

                image_bytes.append(image_byte)
                image_labels.append(label_index)

            label_index += 1
    print("Image Count: %d" % len(image_bytes))
    print("Label Count: %d" % len(image_labels))
    return train_model(image_bytes, image_labels)


def train_model(image_bytes, image_labels):
    if len(image_bytes) != len(image_labels):
        raise NotMatchCountError("画像枚数とラベル数が一致しません")

    # NumPy配列化
    train_images = np.array(image_bytes)/255.0
    train_labels = np.array(image_labels)
    print(train_images.shape)
    print(train_labels.shape)

    # ???????
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(
            FIXED_IMAGE_SIZE, FIXED_IMAGE_SIZE, 3)),
        keras.layers.Dense(256, activation=tf.nn.relu),
        keras.layers.Dense(len(CLASS_NAMES), activation=tf.nn.softmax)
    ])
    model.compile(optimizer=tf.train.AdamOptimizer(),
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    model.fit(train_images, train_labels, epochs=50)
    return model


def test(model, *image_paths):
    image_bytes = []
    for image_path in image_paths:
        image_byte = cv2.imread(image_path, cv2.IMREAD_COLOR)
        image_byte = cv2.resize(
            image_byte, (FIXED_IMAGE_SIZE, FIXED_IMAGE_SIZE))

        image_bytes.append(image_byte)

    test_images = np.array(image_bytes)/255.0
    predictions = model.predict(test_images)
    return predictions


if __name__ == "__main__":
    print("===> START")
    model = main(PROC_PATHS, IMG_DIR_NAMES)

    predictions = test(model, "10.jpg")
    photo_num = 1
    for prediction in predictions:
        print("")
        print("--- photo%d.png ---------" % photo_num)
        i = 0
        for r in prediction:
            s = "%.10f" % r
            print("%s\t:\t%f％(%s)" % (CLASS_NAMES[i], (float(s) * 100), r))
            i += 1
        photo_num += 1

    print("===> FINISH")