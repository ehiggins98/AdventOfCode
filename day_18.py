import copy

increments = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def input():
    area = []
    with open('input.txt') as f:
        line = f.readline()

        while line:
            area.append(list(line)[:-1])
            line = f.readline()
    return area

def adjacent(type, row, col, area):
    adjacent = 0
    for inc in increments:
        if row + inc[0] >= 0 and row + inc[0] < len(area) and col + inc[1] >= 0 and col + inc[1] < len(area[row]) and area[row + inc[0]][col + inc[1]] == type:
            adjacent += 1
    return adjacent

def next_contents(woods, lumberyards, current):
    if current == '.' and woods >= 3:
        return '|'
    if current == '|' and lumberyards >= 3:
        return '#'
    if current == '#' and lumberyards >= 1 and woods >= 1:
        return '#'
    if current == '#' and (lumberyards == 0 or woods == 0):
        return '.'
    else:
        return current

def value(area):
    woods = 0
    lumberyards = 0
    for row in range(len(area)):
        woods += sum([1 for e in area[row] if e == '|'])
        lumberyards += sum([1 for e in area[row] if e == '#'])
    return woods * lumberyards

def part1():
    area = input()
    for _ in range(10):
        initial = copy.deepcopy(area)
        for row in range(len(area)):
            for col in range(len(area[row])):
                woods = adjacent('|', row, col, initial)
                lumberyards = adjacent('#', row, col, initial)
                area[row][col] = next_contents(woods, lumberyards, initial[row][col])
    
    print(value(area))

def part2():
    area = input()
    for i in range(4000):
        initial = copy.deepcopy(area)
        for row in range(len(area)):
            for col in range(len(area[row])):
                woods = adjacent('|', row, col, initial)
                lumberyards = adjacent('#', row, col, initial)
                area[row][col] = next_contents(woods, lumberyards, initial[row][col])
        val = value(area)
        print(i, val)