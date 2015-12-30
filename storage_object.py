"""
Storage object used to store data scanned from text corpus.  This object has
methods to save and load to/from a file.

Data structure:

{
    (Predictor_word_1, ... Predictor_word_n) : [Word_option_1, Word_option_2]
}

"""

import sqlite3
import os

class MarkovStorage(object):
    def __init__(self, markov_order, database_path=None):
        self.data = {}
        self.database_path = database_path
        self.markov_order = markov_order

        #Initialize the database table
        self.init_table()
        print("Created and Initialized Database and Table.")

    def add(self, markov_tuple, word):
        """
        Method to add a tuple and word to data structure
        :param markov_tuple: A tuple containing predictor words.
        :param word: Word option.
        """
        try:
            word_list = self.data[markov_tuple]
            if word not in word_list:
                word_list.append(word)

        except KeyError:
            self.data[markov_tuple] = [word]

    def init_table(self):
        """
        Method which checks whether or not a database file has been created.  Creates one if not
        and then initializes the markov table.
        :return:
        """
        # Create database and tables
        db_created = self._create_database_file()
        if not db_created:
            raise RuntimeError("Something went wrong while creating the database file.")
        self._create_tables()

    def save(self):
        """
        Dumps contents of self.data to the database and clears data from memory.
        """
        # format data in list of lists
        sql_data_list = []
        for predictor in self.data.keys():
            for word_option in self.data[predictor]:
                db_combo = list(predictor)
                db_combo.insert(0, word_option)
                sql_data_list.append(db_combo)

        # Generate main sql statement
        predictor_columns = ["pc_{}".format(x+1) for x in range(self.markov_order)]
        question_marks = "?," * (self.markov_order)
        predictor_column_string = str(predictor_columns)[1:len(str(predictor_columns))-1].replace("'", "")
        sql_statement = "INSERT OR REPLACE INTO markov (word_option, {}) VALUES ({}?)".format(predictor_column_string, question_marks)

        # Execute statements
        cnxn = sqlite3.connect(self.database_path)
        cnxn.executemany(sql_statement, sql_data_list)
        cnxn.commit()
        cnxn.close()

        # Reset data
        del(self.data)
        self.data = {}

    def _create_database_file(self):
        self._touch(self.database_path)
        return True

    @staticmethod
    def _touch(fname):
        """
        Create database file if not there
        https://stackoverflow.com/questions/1158076/implement-touch-using-python
        """
        try:
            os.utime(fname, None)
        except:
            open(fname, 'a').close()

    def _create_tables(self):
        predictor_columns = ["pc_{} TEXT".format(x+1) for x in range(self.markov_order)]
        predictor_unique = ["pc_{}".format(x+1) for x in range(self.markov_order)]
        predictor_column_string = str(predictor_columns)[1:len(str(predictor_columns))-1].replace("'", "")
        predictor_unique_string = str(predictor_unique)[1:len(str(predictor_unique))-1].replace("'", "")
        sql_statement = "CREATE TABLE markov (word_option TEXT, {}, UNIQUE(word_option,{}))".format(
                predictor_column_string,
                predictor_unique_string
        )

        cnxn = sqlite3.connect(self.database_path)
        try:
            cnxn.execute("DROP TABLE markov")
        except sqlite3.OperationalError:
            pass
        cnxn.execute(sql_statement)
        cnxn.commit()
        cnxn.close()
        return self.database_path
