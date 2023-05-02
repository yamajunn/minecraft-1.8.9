import cv2
import numpy as np
import os

input_folder = "default-textures"
output_folder = "default-textures"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(".png"):
        filepath = os.path.join(input_folder, filename)
        img = cv2.imread(filepath, cv2.IMREAD_UNCHANGED)
        if img.shape[2] == 3:  # RGB画像の場合
            img_rgba = cv2.cvtColor(img, cv2.COLOR_RGB2RGBA)
            cv2.imwrite(os.path.join(output_folder, filename), img_rgba)
        else:  # RGBA画像の場合
            cv2.imwrite(os.path.join(output_folder, filename), img)
