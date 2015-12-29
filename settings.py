import os

# Location of folder which contains corpus of text to scan.
TEXT_FILE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'text_files')

# File to dump storage object into.
MARKOV_STORAGE_FILE_PATH = 'markov_dump.txt'
