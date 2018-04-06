import random 
nothing = 0 #ничего
rock = 1 #скала
shrimp = 2 #креветка
fish = 3 #рыба
animals = []
loneliness = []
loneliness.append(2)
loneliness.append(2)
many = []
ocean = []
save_ocean = []
new_ocean = []
sub_ocean = []
many.append(4)
many.append(4)
animals.append(shrimp)
animals.append(fish)
whole = []
whole.append(nothing)
whole.append(rock)
whole.append(shrimp)
whole.append(fish)
select = 0
def neighborhood(this, N, S, W, E, NW, NE, SW, SE):
   neighbors = 0
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
   return(neighbors)  
def generation(animal, N, S, W, E, NW, NE, SW, SE):
   count = 0
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
   return(count)
def random(width, length, maximal):
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
def read(width, length):
  new_list = []
  new_list.append([0] * (width + 2))
  for i in range(0, length):
    events = [0]
    events = events + map(int, input().split(' '))
    events = events + [0]
    new_list.append(events)
  new_list.append([0] * (width + 2))   
  return new_list  
def whitespace(width, length):
  list = []
  list.append([0] * (width + 2))
  for i in range(0, length):
    subevents = [0] * (length + 2)
    list.append(subevents)
  list.append([0] * (width + 2))
  return list
while (select != 3):
  print("МЕНЮ:")
  print("1 - запустить игру")
  print("2 - добавить животное")
  print("3 - выход")
  select = int(input())
  if (select == 1):
    print("Введите количество поколений")
    number_of_generations = int(input())
    print("Введите размеры океана")
    length, width = input().split(' ')
    length = int(length)
    width = int(width)
    print("1 - сгенерировать произвольное положение океана")
    print("2 - загрузить сохраненное положение океана")
    print("3 - ввести собственное положение океана")
    third_select = int(input())
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
    for q in range (0, number_of_generations):
      for i in range(1, length - 1):
        for j in range(1, width - 1):
             neighbors =  neighborhood(ocean[i][j], ocean[i - 1][j - 1],
             ocean[i - 1][j], ocean[i - 1][j + 1], ocean[i][j - 1],
             ocean[i][j + 1], ocean[i + 1][j - 1], ocean[i + 1][j],
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
                   neighbors_animals[k] = generation(animals[k], ocean[i - 1][j - 1],
             ocean[i - 1][j], ocean[i - 1][j + 1], ocean[i][j - 1],
             ocean[i][j + 1], ocean[i + 1][j - 1], ocean[i + 1][j],
             ocean[i + 1][j + 1])
                if (neighbors_animals.count(3) > 0):
                  new_ocean[i][j] = animals[neighbors_animals.index(3)]
    ocean = new_ocean
    sub_ocean = new_ocean
    ocean.pop(length - 1)
    ocean.pop(0)
    for c in range(0, length - 2):
       ocean[c].pop(0)
       ocean[c].pop(width - 2)
    for row in ocean:
      print(' '.join([str(elem) for elem in row]))
    print("1 - сохранить текущее состояние океана")
    print("2 - продолжить игру")
    second_select = int(input())
    if (second_select == 1):
      save_ocean = sub_ocean
    if (second_select == 2):
      ocean = []
      new_ocean = []
      sub_ocean = []
  if (select == 2):
    new_animal = len(animals) + 1
    print("Вы добавили животное под номером:")
    print(new_animal)
    print("Введите минимально допустимое число соседей этого же вида:")
    few = int(input())
    loneliness.append(few)
    print("Введите максимально допустимое число соседей этого же вида:")
    most = int(input())
    whole.append(new_animal)
    many.append(most)
    animals.append(new_animal)
