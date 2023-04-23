import os.path
from threading import Thread
from time import time

import requests as re


def get_img_urls(file_path):
    with open(file_path, "r") as f:
        return [line.rstrip().replace("\'", "") for line in f]


def download(url, where, new_file_name):
    print(f'url is = {url}')
    response = re.get(url)
    with open(os.path.join(where, new_file_name), "wb") as f:
        chunk_size = 1024
        for bytes_chunk in response.iter_content(chunk_size):
            f.write(bytes_chunk)


if __name__ == "__main__":
    file_path = r'Z:\___advanced python\list_of_images.txt'
    url_idx = 0
    downloads_folder = "downloads_threads"
    threads = []
    before = time()
    for url in get_img_urls(file_path):
        new_file_name = "img_" + str(url_idx) + ".jpg"
        thread = Thread(target=download, args=(url, downloads_folder, new_file_name,))
        threads.append(thread)
        url_idx += 1

    [t.start() for t in threads]
    [t.join() for t in threads]
    after = time()

    print(f"Total time = {after - before}")




