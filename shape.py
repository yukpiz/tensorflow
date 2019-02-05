import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images,
                               test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# モデルを学習する前にデータセットのフォーマットを調べてみましょう。次の図は、トレーニングセットに6万枚の画像があり、各画像は28 x 28ピクセルで表されることを示しています。

print("Training Images ---")
print(train_images.shape)
print(train_labels.shape)
print(type(train_images.shape))
print(type(train_labels.shape))

print("Test Images ---")
print(test_images.shape)
print(test_labels.shape)
print(type(test_images.shape))
print(type(test_labels.shape))