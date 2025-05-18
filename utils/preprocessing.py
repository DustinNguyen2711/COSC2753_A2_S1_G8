import os
import shutil
from PIL import Image

def clean_and_resize_images(source_dir, target_dir, size=(224, 224)):
    os.makedirs(target_dir, exist_ok=True)
    invalid_images = []

    for class_name in os.listdir(source_dir):
        class_path = os.path.join(source_dir, class_name)
        target_class_path = os.path.join(target_dir, class_name)
        os.makedirs(target_class_path, exist_ok=True)

        for img_name in os.listdir(class_path):
            img_path = os.path.join(class_path, img_name)
            try:
                img = Image.open(img_path)
                img.verify()
                img = Image.open(img_path).convert("RGB").resize(size)
                img.save(os.path.join(target_class_path, img_name))
            except:
                invalid_images.append(img_path)

    return invalid_images
