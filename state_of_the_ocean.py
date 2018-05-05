import argparse


parser = argparse.ArgumentParser(description = 'Process some integers.')
parser.add_argument('-m', '--model', type = str)


def random(width, length, maximal):  # функция рандомного первичного состояния океана
    import random
    new_list = []
    new_list.append([0] * (width + 2))
    for i in range(0, length):
        events = [0]
        for j in range(0, width):
            events = events + [random.randint(0, maximal)]
            events = events + [0]
        new_list.append(events)
    new_list.append([0] * (width + 2))
    return new_list


def read(width, length):  # функция чтения пользовательского начального состояния океана
    new_list = []
    new_list.append([0] * (width + 2))
    for i in range(0, length):
        events = [0]
        options = parser.parse_args()
        infile = options.model
        events = events + infile
        events = events + [0]
        new_list.append(events)
    new_list.append([0] * (width + 2))
    return new_list


def whitespace(width, length):  # функция, генерирующая "чистый" океан для заполнения
    list = []  # следующей итерации
    list.append([0] * (width + 2))
    for i in range(0, length):
        subevents = [0] * (length + 2)
        list.append(subevents)
    list.append([0] * (width + 2))
    return list
