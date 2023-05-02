import os
import cv2
import numpy as np

path = "./default-textures"
files = os.listdir(path)

for file in files:

    if file != ".DS_Store":

        img = cv2.imread(f'default-textures/{file}', cv2.IMREAD_UNCHANGED)

        h, w = img.shape[:2]

        alpha_list = []
        bgr_list = [0, 0, 0]

        print(file)
        for i in range(h):
            for j in range(w):
                b, g, r, a = img[i, j]
                alpha_list.append(a)
                bgr_list[0] += b
                bgr_list[1] += g
                bgr_list[2] += r

        bgr_list[0] = int(bgr_list[0]/(h*w))
        bgr_list[1] = int(bgr_list[1]/(h*w))
        bgr_list[2] = int(bgr_list[2]/(h*w))

        for i in range(h):
            for j in range(w):
                img[i, j] = bgr_list[0], bgr_list[1], bgr_list[2], alpha_list[i*j+j]

        cv2.imwrite(f'blocks/{file}',img)