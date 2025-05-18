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


import os
import shutil
import random

def split_train_val(base_dir, train_ratio=0.8, seed=42):
    train_dir = os.path.join(base_dir, "train")
    val_dir = os.path.join(base_dir, "val")
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)

    random.seed(seed)
    for class_name in os.listdir(base_dir):
        class_path = os.path.join(base_dir, class_name)
        if not os.path.isdir(class_path):
            continue

        images = os.listdir(class_path)
        random.shuffle(images)
        split_idx = int(len(images) * train_ratio)
        train_images = images[:split_idx]
        val_images = images[split_idx:]

        os.makedirs(os.path.join(train_dir, class_name), exist_ok=True)
        os.makedirs(os.path.join(val_dir, class_name), exist_ok=True)

        for img in train_images:
            shutil.copy2(os.path.join(class_path, img), os.path.join(train_dir, class_name, img))
        for img in val_images:
            shutil.copy2(os.path.join(class_path, img), os.path.join(val_dir, class_name, img))
