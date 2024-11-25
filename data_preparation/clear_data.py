import os
import hashlib
from concurrent.futures import ThreadPoolExecutor
import threading
from tqdm import tqdm
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def compute_hash(file_path):
    """Compute the MD5 hash of a file."""
    md5 = hashlib.md5()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            md5.update(chunk)
    return md5.hexdigest()

def process_file(file_path, hash_dict, lock, labels_directory, removed_count):
    """Process a single file and update the hash dictionary."""
    if os.path.isfile(file_path) and file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        file_hash = compute_hash(file_path)
        with lock:
            if file_hash in hash_dict:
                os.remove(file_path)
                # Remove the corresponding label file
                label_file = os.path.join(labels_directory, os.path.basename(file_path).rsplit('.', 1)[0] + '.txt')
                if os.path.exists(label_file):
                    os.remove(label_file)
                removed_count[0] += 1
            else:
                hash_dict[file_hash] = file_path

def remove_duplicate_images(image_directory, labels_directory, max_workers=4):
    """Remove duplicate images and their labels from the specified directories using multi-threading."""
    hash_dict = {}
    lock = threading.Lock()
    removed_count = [0]
    file_list = [os.path.join(image_directory, filename) for filename in os.listdir(image_directory)]

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        list(tqdm(executor.map(lambda file_path: process_file(file_path, hash_dict, lock, labels_directory, removed_count), file_list), total=len(file_list)))

    logging.info(f"Removed {removed_count[0]} duplicate images and their labels.")

# Specify the directories containing the images and labels
image_directory = 'images'
labels_directory = 'labels'

# Remove duplicate images and their labels
remove_duplicate_images(image_directory, labels_directory)