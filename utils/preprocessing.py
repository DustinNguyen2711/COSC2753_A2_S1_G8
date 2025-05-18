import os
import shutil
from typing import List, Tuple
from PIL import Image

def clean_and_resize_images(source_dir: str, target_dir: str, size: Tuple[int, int] = (224, 224)) -> List[str]:
    invalid_images = []
    os.makedirs(target_dir, exist_ok=True)

    for class_name in os.listdir(source_dir):
        class_path = os.path.join(source_dir, class_name)
        target_class_path = os.path.join(target_dir, class_name)
        os.makedirs(target_class_path, exist_ok=True)

        for img_name in os.listdir(class_path):
            img_path = os.path.join(class_path, img_name)
            try:
                img = Image.open(img_path).convert("RGB")
                img = img.resize(size)
                img.save(os.path.join(target_class_path, img_name))
            except Exception:
                invalid_images.append(img_path)

    return invalid_images

def split_train_val(base_dir: str, train_ratio: float = 0.8, seed: int = 42) -> None:
    import random
    random.seed(seed)

    train_dir = os.path.join(base_dir, "train")
    val_dir = os.path.join(base_dir, "val")

    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)

    for class_name in os.listdir(base_dir):
        class_path = os.path.join(base_dir, class_name)
        if not os.path.isdir(class_path) or class_name in ["train", "val"]:
            continue

        images = os.listdir(class_path)
        random.shuffle(images)
        split_idx = int(len(images) * train_ratio)
        train_images = images[:split_idx]
        val_images = images[split_idx:]

        os.makedirs(os.path.join(train_dir, class_name), exist_ok=True)
        os.makedirs(os.path.join(val_dir, class_name), exist_ok=True)

        for img in train_images:
            src = os.path.join(class_path, img)
            dst = os.path.join(train_dir, class_name, img)
            try:
                shutil.copy2(src, dst)
            except PermissionError:
                print(f"PermissionError: Cannot copy {src}")

        for img in val_images:
            src = os.path.join(class_path, img)
            dst = os.path.join(val_dir, class_name, img)
            try:
                shutil.copy2(src, dst)
            except PermissionError:
                print(f"PermissionError: Cannot copy {src}")