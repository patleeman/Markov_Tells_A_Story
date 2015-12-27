"""
The schema consists of a tuple containing the prior n words to an index 0 word.

storage schema = {
    (word(n-m), word(n-2), word(n-1)): [word(n)],
    (word(n-m), word(n-2), word(n-1)): [word(n)],
}
"""
def scan(storage_object, data_file, markov_order=2):
    with open(data_file) as f:
        text = f.read()

    marked_text = replace_punctuation(text)

    sentences = marked_text.split("<EOS>")
    for sentence in sentences:
        sentence_content = sentence.split("<SPACE>")

        for i, current_word in enumerate(sentence_content):
            if current_word == "<SPACE>":
                continue

            if current_word == "":
                del(sentence_content[i])
                continue

            if i < markov_order + 1:
                continue

            markov_tuple_index = {i-x for x in range(markov_order + 1) if x != 0}
            markov_tuple = tuple([convert_punctuation(sentence_content[x]) for x in markov_tuple_index])
            storage_object.add(markov_tuple, convert_punctuation(current_word))

    return storage_object


def convert_punctuation(text):
    replacement = {
            "<PERIOD>": ".",
            "<COMMA>": ",",
            "<SEMICOLON>": ";",
            "<COLON>": ":",
            "<EXCLAMATION>": "!",
            "<QUESTION>": "?",
        }

    new_text = text
    for item in replacement.keys():
        new_text = new_text.replace(item, replacement[item])

    return new_text


def replace_punctuation(text):
    # Dict indicating the replacement of key punctuation marks.
    replacement = {
        ".": "<SPACE><PERIOD><EOS>",
        ",": "<SPACE><COMMA>",
        ";": "<SPACE><SEMICOLON>",
        ":": "<SPACE><COLON>",
        "!": "<SPACE><EXCLAMATION><EOS>",
        "?": "<SPACE><QUESTION><EOS>",
        " ": "<SPACE>",
        "\n": "<SPACE>",
        "\t": "<SPACE>",
        "\r": "",
        '"': "",
    }
    new_text = text
    for item in replacement.keys():
        new_text = new_text.replace(item, replacement[item])
    return new_text


if __name__ == '__main__':
    from storage_object import MarkovStorage
    storage_object = MarkovStorage()
    storage_object = scan(storage_object, 'test.txt', markov_order=3)
    print(storage_object.data)

