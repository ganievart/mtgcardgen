from textgenrnn import textgenrnn

textgen = textgenrnn()
textgen.train_from_file('names.txt', num_epochs=1)
textgen.generate()


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')
