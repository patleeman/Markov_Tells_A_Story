import json

class MarkovStorage(object):
    def __init__(self, file_path=None):
        self.data = {}
        self.file_path = file_path

    def save(self, file_path=None):
        if not file_path:
            self.file_path = file_path
        with open(self.file_path, 'w+') as f:
            f.write(json.dumps(self.data))

    def load(self, file_path=None):
        if not file_path:
            self.file_path = file_path
        with open(self.file_path) as f:
            self.data = json.loads(f.read())

    def add(self, markov_tuple, word):
        try:
            word_list = self.data[markov_tuple]
            if word not in word_list:
                word_list.append(word)

        except KeyError:
            self.data[markov_tuple] = [word]



