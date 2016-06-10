import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# Location of folder which contains corpus of text to scan.
TEXT_FILE_FOLDER = os.path.join(BASE_PATH, 'text_files')


MARKOV_DATABASE_FILE_PATH = os.path.join(BASE_PATH, 'database', 'markov_db.sqlite3')

# Markov Order
MARKOV_ORDER = 2

DB_TRANSACTION_INTERVAL = 25

