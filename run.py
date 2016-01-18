#!/usr/bin/python3

from tqdm import tqdm
import scanner
import storage_object
from settings import *
import time

def scan_folder_contents(folder_path):
    start = time.time()
    folder_contents = os.listdir(folder_path)
    # Initialize database:
    storage = storage_object.MarkovStorage(markov_order=MARKOV_ORDER, database_path=MARKOV_DATABASE_FILE_PATH)

    for i, file in enumerate(tqdm(folder_contents)):
        path = os.path.join(TEXT_FILE_FOLDER, file)
        storage = scanner.scan(storage, path, markov_order=MARKOV_ORDER)

        if i % DB_TRANSACTION_INTERVAL == 0:
            storage.save()

    if storage.data is not None:
        storage.save()

    end = time.time() - start
    print("Complete {}".format(end))
    return

if __name__ == '__main__':
    scan_folder_contents(TEXT_FILE_FOLDER)
