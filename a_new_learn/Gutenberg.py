import kim


def count_words(filename):
    """Open the file"""

    try:
        with open(filename) as file_object:
            contens = file_object.read()
    except FileNotFoundError:
        pass
    else:
        the_num = contens.count('the')
        print(str(the_num))


filename = 'cats_name.txt'
count_words(filename)
