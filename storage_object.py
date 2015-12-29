
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
        try:
            word_list = self.data[markov_tuple]
            if word not in word_list:
                word_list.append(word)

        except KeyError:
            self.data[markov_tuple] = [word]



