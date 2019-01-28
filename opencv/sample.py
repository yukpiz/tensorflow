#codeing:utf-8

import numpy as np
import cv2

img = cv2.imread("data/src/photo1.jpg");
cv2.imshow("作成するウィンドウ名(なんでもいい)",img)
cv2.waitKey()