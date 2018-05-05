def neighborhood(this, N, S, W, E, NW, NE, SW, SE):  # функция, подсчитывающая число соседей
    neighbors = 0  # этого же вида
    if (N == this):
        neighbors += 1
    if (S == this):
        neighbors += 1
    if (W == this):
        neighbors += 1
    if (E == this):
        neighbors += 1
    if (NW == this):
        neighbors += 1
    if (NE == this):
        neighbors += 1
    if (SW == this):
        neighbors += 1
    if (SE == this):
        neighbors += 1
    return (neighbors)


def generation(animal, N, S, W, E, NW, NE, SW, SE):  # функция, проверяющая, должно ли
    count = 0  # появиться существо в пустой клетке
    if (N == animal):
        count += 1
    if (S == animal):
        count += 1
    if (W == animal):
        count += 1
    if (E == animal):
        count += 1
    if (NW == animal):
        count += 1
    if (NE == animal):
        count += 1
    if (SW == animal):
        count += 1
    if (SE == animal):
        count += 1
    return (count)
