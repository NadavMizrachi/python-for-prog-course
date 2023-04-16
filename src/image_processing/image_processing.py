import os
import time
from PIL import Image, ImageFilter

images_dir = "images"


def create_thumbnail(file_name, size=(50, 50), thumb_dir='thumbs'):
    img = Image.open(os.path.join(images_dir, file_name))
    img = img.filter(ImageFilter.GaussianBlur())
    img.thumbnail(size)
    img.save(os.path.join(thumb_dir, file_name))

if __name__ == "__main__":
    images_names = os.listdir(images_dir)
    print(images_names)
    tic = time.time()
    for image_name in images_names:
        create_thumbnail(image_name)
    toc = time.time()
    print(f"Time for processing {toc - tic}")