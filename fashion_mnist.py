import tensorflow as tf
from tensorflow import keras

print(tf.__version__)

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

print(train_images)
print(train_labels)
print(test_images)
print(test_labels)
