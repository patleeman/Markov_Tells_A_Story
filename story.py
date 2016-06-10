import sqlite3
import os
import random

def generate_sentence():
    dbase_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database', 'markov_db.sqlite3')
    sentence = grab_seed()
    output_data = []
    with dbase(dbase_path) as db:
        sentence_end = ['.', '!', '?']
        while True:
            query = "SELECT word_option FROM markov WHERE pc_1='{}' AND pc_2='{}'".format(sentence[-2], sentence[-1])
            words = db.select(query)

            # Clean up the database output
            words = [word[0] for word in words]

            if not words:
                sentence.append('.')
                break
            else:
                new_word = random.choice(words)
                sentence.append(new_word.lower())

        complete_sentence = " ".join(sentence).capitalize()
        output_data.append(complete_sentence)

        return output_data


def grab_seed():
    dbase_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database', 'markov_db.sqlite3')
    with dbase(dbase_path) as db:
        data = db.select("SELECT * FROM markov")
        seed = random.choice(data)
    return list(seed[1:])


class dbase():
    def __init__(self, database):
        self.cnxn = sqlite3.connect(database)
        self.cursor = self.cnxn.cursor()

    def __enter__(self):
        return self

    def select(self, statement):
        self.cursor.execute(statement)
        data = self.cursor.fetchall()
        return data

    def __exit__(self, exc_type, exc_value, traceback):
        self.cnxn.close()

if __name__ == "__main__":
    data = generate_sentence()
    print(data)