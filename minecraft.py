import os
import cv2
import numpy as np

path = "./default-textures"
files = os.listdir(path)

for file in files:

    base, ext = os.path.splitext(file)

    if ext == ".png":

        img = cv2.imread(f'default-textures/{file}', flags = cv2.IMREAD_UNCHANGED)

        h, w = img.shape[:2]
        r_count = 0
        g_count = 0
        b_count = 0
        count = 0

        for i in range(h):
            for j in range(w):
                b, g, r, a = img[i, j]
                if a != 0:
                    r_count += r
                    g_count += g
                    b_count += b
                    count += 1
        
        r_average = 0
        g_average = 0
        b_average = 0

        if count != 0:
            r_average = int(r_count/count)
            g_average = int(g_count/count)
            b_average = int(b_count/count)

        for i in range(h):
            for j in range(w):
                b, g, r, a = img[i, j]
                img[i, j] = b_average, g_average, r_average, a

        cv2.imwrite(f'blocks/{file}',img)