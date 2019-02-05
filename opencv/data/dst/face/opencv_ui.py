#codeing:utf-8

import cv2
import sys, os, glob, imghdr

DIRS = [
    "0_sakura_minamoto",
    "1_saki_nikaido",
    "2_ai_mizuno",
    "3_junko_konno",
    "4_yugiri",
    "5_lily_hoshikawa",
    "6_tae_yamada",
    "7_kotaro_tatsumi",
]

def main(src_path):
    for image_path in glob.glob('{}/*.*'.format(src_path), recursive=False):
        quit = False
        if imghdr.what(image_path) is None:
            continue
        print("Read: %s" % image_path)
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        image = cv2.resize(image, (400, 400))

        cv2.imshow("image", image)

        while True:
            key = cv2.waitKey(0)
            print(key)
            i = None
            if key == 27: # esc
                quit = True
                cv2.destroyAllWindows()
                break
            elif key == 48: # 0
                i = 0
            elif key == 49: # 1
                i = 1
            elif key == 50: # 2
                i = 2
            elif key == 51: # 3
                i = 3
            elif key == 52: # 4
                i = 4
            elif key == 53: # 5
                i = 5
            elif key == 54: # 6
                i = 6
            elif key == 55: # 7
                i = 7
            elif key == 115: # s
                print("Skip %s" % image_path)
                break # skip
            elif key == 100: # d
                print("Delete %s" % image_path)
                delete(image_path) # delete
                break
            if i != None:
                move(image_path, DIRS[i])
                break
        if quit:
            break

    cv2.destroyAllWindows()

def delete(image_path):
    os.remove(image_path)

def move(src_file_path, dst_path):
    image = cv2.imread(src_file_path, cv2.IMREAD_COLOR)
    if not os.path.isdir(dst_path):
        os.makedirs(dst_path)
    new_image_path = dst_path + "/" + os.path.basename(src_file_path)
    cv2.imwrite(new_image_path, image)
    delete(src_file_path)
    print("Move to %s" % new_image_path)


if __name__ == "__main__":
    main(".")


