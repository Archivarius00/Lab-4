

items = [
    ['r',25,3],
    ['p',15,2],
    ['a',15,2],
    ['m',20,2],
    ['i',5,1],
    ['k',15,1],
    ['x',20,3],
    ['t',25,1], 
    ['f',15,1],
    ['d',10,1],
    ['s',20,2],
    ['c',20,2]
]


slots = 8
n = 0
points = 15
backpack = []
backpack.append('d')


points += [x for x in items if x[0] == 'd'][0][1]
inventory = [x for x in items if x[0] == 'd'][0][2]
space = slots - inventory

items = [x for x in items if x[0] != 'd']
items.sort(key=lambda row: (row[2]))
items.sort(key=lambda row: (row[1]),reverse = True)



for x in items:
    n += 1
    if x[2] <= space:
        backpack.append(x[0])
        points += x[1]
        space -= x[2]


print(f"Инвентарь: {backpack}")
print('Очки выживания:', points)
