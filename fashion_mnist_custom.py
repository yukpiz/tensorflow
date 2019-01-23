import tensorflow as tf
from tensorflow import keras
from PIL import Image

import numpy as np
import matplotlib.pyplot as plt



fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

print(len(train_images))
print(len(train_labels))
print(len(test_images))
print(len(test_labels))

#print(train_images[0])
print(train_labels[0])
print(train_labels[1])

pil_img = Image.fromarray(train_images[0])
pil_img.save('sample.png')
