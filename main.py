import random
import argparse
import state_of_the_ocean
import position

nothing = 0  # ничего
rock = 1  # скала
shrimp = 2  # креветка
fish = 3  # рыба

animals = [shrimp, fish]  # инициализация массивов
loneliness = [2, 2]
many = [4, 4]
ocean = []
save_ocean = []
new_ocean = []
whole = [shrimp, fish, nothing, rock, shrimp, fish]
select = 0


while (select != 3):
    print("МЕНЮ:")
    print("1 - запустить игру")
    print("2 - добавить животное")
    print("3 - выход")
    options = parser.parse_args()
    select = options.model
    select = int(select)
    if (select == 1):
        print("Введите количество поколений")
        options = parser.parse_args()
        number_of_generations = options.model
        number_of_generations = int(number_of_generations)
        print("Введите длину океана")
        options = parser.parse_args()
        length = options.model
        length = int(length)
        print("Введите длину океана")
        options = parser.parse_args()
        width = options.model
        width = int(width)
        print("1 - сгенерировать произвольное положение океана")
        print("2 - загрузить сохраненное положение океана")
        print("3 - ввести собственное положение океана")
        options = parser.parse_args()
        third_select = options.model
        third_select = int(third_select)
        if (third_select == 1):
            maximal = len(whole)
            ocean = random(width, length, maximal)
            new_ocean = whitespace(width, length)
        if (third_select == 2):
            ocean = []
            new_ocean = []
            ocean.append([0] * (width + 2))
            new_ocean.append([0] * (width + 2))
            for i in range(0, length):
                ocean.append([0] + save_ocean[i] + [0])
                subevents = [0] * (length + 2)
                new_ocean.append(subevents)
            ocean.append([0] * (width + 2))
            new_ocean.append([0] * (width + 2))
        if (third_select == 3):
            print("Введите начальное состояние океана")
            ocean = read(width, length)
            new_ocean = whitespace(width, length)
        length += 2
        width += 2
        count_animals = len(animals)
        for q in range(0, number_of_generations):
            for i in range(1, length - 1):
                for j in range(1, width - 1):
                    neighbors = neighborhood(
                        ocean[i][j], ocean[i - 1][j - 1],
                        ocean[i - 1][j], ocean[i - 1][j + 1],
                        ocean[i][j - 1], ocean[i][j + 1],
                        ocean[i + 1][j - 1], ocean[i + 1][j],
                        ocean[i + 1][j + 1])
                    if (animals.count(ocean[i][j]) > 0):
                        if (neighbors >= many[animals.index(ocean[i][j])]):
                            new_ocean[i][j] = nothing
                        if (neighbors < loneliness[animals.index(ocean[i][j])]):
                            new_ocean[i][j] = nothing
                        if (neighbors < many[animals.index(ocean[i][j])]):
                            if (neighbors >= loneliness[animals.index(ocean[i][j])]):
                                new_ocean[i][j] = ocean[i][j]
                    if (ocean[i][j] == rock):
                        new_ocean[i][j] = ocean[i][j]
                    if (ocean[i][j] == nothing):
                        neighbors_animals = [0] * count_animals
                        for k in range(0, count_animals):
                            neighbors_animals[k] = generation(
                                animals[k], ocean[i - 1][j - 1],
                                ocean[i - 1][j], ocean[i - 1][j + 1],
                                ocean[i][j - 1], ocean[i][j + 1],
                                ocean[i + 1][j - 1], ocean[i + 1][j],
                                ocean[i + 1][j + 1])
                        if (neighbors_animals.count(3) > 0):
                            new_ocean[i][j] = animals[neighbors_animals.index(3)]
        ocean = new_ocean
        ocean.pop(length - 1)
        ocean.pop(0)
        for c in range(0, length - 2):
            ocean[c].pop(0)
            ocean[c].pop(width - 2)
        for row in ocean:
            print(' '.join([str(elem) for elem in row]))
        print("1 - сохранить текущее состояние океана")
        print("2 - продолжить игру")
        options = parser.parse_args()
        second_select = options.model
        second_select = int(second_select)
        if (second_select == 1):
            save_ocean = []
            save_ocean.append([0] * (width + 2))
            for i in range(0, length - 2):
                events = [0]
                events = events + ocean[i]
                events = events + [0]
            save_ocean.append(events)
            save_ocean.append([0] * (width + 2))
        if (second_select == 2):
            ocean = []
            new_ocean = []
    if (select == 2):
        new_animal = len(animals) + 1
        print("Вы добавили животное под номером:")
        print(new_animal)
        print("Введите минимально допустимое число соседей этого же вида:")
        print("Введите длину океана")
        options = parser.parse_args()
        few = options.model
        few = int(few)
        loneliness.append(few)
        print("Введите максимально допустимое число соседей этого же вида:")
        options = parser.parse_args()
        most = options.model
        most = int(most)
        whole.append(new_animal)
        many.append(most)
        animals.append(new_animal)
