"""
Storage object used to store data scanned from text corpus.  This object has
methods to save and load to/from a file.

Data structure:

{
    (Predictor_word_1, ... Predictor_word_n) : [Word_option_1, Word_option_2]
}

"""
class MarkovStorage(object):
    def __init__(self, file_path=None):
        self.data = {}
        self.file_path = file_path

    def save(self):
        with open(self.file_path, 'w+') as f:
            f.write(str(self.data))

    def load(self):
        with open(self.file_path) as f:
            self.data = eval(f.read())

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



