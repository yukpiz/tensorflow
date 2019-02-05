import cv2
import glob
import os

source_path = './data/src/'
output_path = './data/dst/movie/'
out_face_path = './data/dst/face/'
xml_path = './lbpcascade_animeface.xml'


def movie_to_image(num_cut, video_name):
    os.mkdir(output_path + video_name)
    capture = cv2.VideoCapture(source_path + video_name)

    img_count = 0
    frame_count = 0

    while(capture.isOpened()):

        ret, frame = capture.read()
        if ret == False:
            break

        if frame_count % num_cut == 0:
            img_file_name = output_path + video_name + \
                '/' + str(img_count) + ".jpg"
            cv2.imwrite(img_file_name, frame)
            img_count += 1

        frame_count += 1

    capture.release()


def face_detect(img_list, video_name):
    os.mkdir(out_face_path + video_name)
    classifier = cv2.CascadeClassifier(xml_path)

    img_count = 1
    for img_path in img_list:
        org_img = cv2.imread(img_path, cv2.IMREAD_COLOR)

        gray_img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

        face_points = classifier.detectMultiScale(gray_img,
                                                  scaleFactor=1.2, minNeighbors=2, minSize=(1, 1))

        for points in face_points:

            x, y, width, height = points

            dst_img = org_img[y:y+height, x:x+width]

            face_img = cv2.resize(dst_img, (64, 64))
            new_img_name = out_face_path + video_name + \
                '/' + str(img_count) + 'face.jpg'
            cv2.imwrite(new_img_name, face_img)
            img_count += 1


video_name = 'zombi1.mp4'
#movie_to_image(int(10), video_name)
images = glob.glob(output_path + video_name + '/*.jpg')
face_detect(images, video_name)

video_name = 'zombi2.mp4'
movie_to_image(int(10), video_name)
images = glob.glob(output_path + video_name + '/*.jpg')
face_detect(images, video_name)

video_name = 'zombi3.mp4'
movie_to_image(int(10), video_name)
images = glob.glob(output_path + video_name + '/*.jpg')
face_detect(images, video_name)
