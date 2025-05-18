from PIL import Image
import numpy as np
import os

def get_average_rgb(image_path):
    img = Image.open(image_path).convert("RGB")
    np_img = np.array(img)
    return np_img.mean(axis=(0, 1))
