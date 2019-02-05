# codeing:utf-8

import cv2

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
    for image_path in glob.glob('{}/**/*.*'.format(src_path), recursive=True):
        print(image_path)


if __name__ == "__main__":
    main(".")
