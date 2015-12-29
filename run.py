from tqdm import tqdm
import scanner
import storage_object
from settings import *


def scan_folder_contents(folder_path):
    folder_contents = os.listdir(folder_path)
    storage_object = create_storage_object(storage_file=MARKOV_STORAGE_FILE_PATH)
    print(MARKOV_STORAGE_FILE_PATH)

    for i, file in enumerate(tqdm(folder_contents)):
        path = os.path.join(TEXT_FILE_FOLDER, file)
        storage_object = scanner.scan(storage_object, path, markov_order=3)
    print(storage_object.data)
    storage_object.save()
    return


def create_storage_object(storage_file):
    markov_storage_object = storage_object.MarkovStorage(file_path=storage_file)
    if not storage_object:
        markov_storage_object.load()
    return markov_storage_object


if __name__ == '__main__':
    scan_folder_contents(TEXT_FILE_FOLDER)