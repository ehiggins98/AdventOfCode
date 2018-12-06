import copy

def file_input():
    coordinates = []
    with open('input.txt') as f:
        line = f.readline()
        while line != '':
            data = line[:-1].split(', ')
            coordinates.append((int(data[0]), int(data[1])))
            line = f.readline()
    return coordinates

def get_closest(x, y, coordinates):
    min_dist = 1000
    argmin = []
    for c in coordinates:
        if abs(x - c[0]) + abs(y - c[1]) < min_dist:
            min_dist = abs(x - c[0]) + abs(y - c[1])
            argmin = [c]
        elif abs(x - c[0]) + abs(y - c[1]) == min_dist:
            argmin.append(c)
    return argmin[0] if len(argmin) == 1 else None

def remove_infinite(coordinates):
    orig = copy.deepcopy(coordinates)
    for x in range(-1, 401):
        closest = get_closest(x, -1, orig)
        if closest in coordinates:
            coordinates.remove(closest)
    for x in range(-1, 401):
        closest = get_closest(x, 401, orig)
        if closest in coordinates:
            coordinates.remove(closest)
    for y in range(-1, 400):
        closest = get_closest(-1, y, orig)
        if closest in coordinates:
            coordinates.remove(closest)
    for y in range(-1, 400):
        closest = get_closest(401, y, orig)
        if closest in coordinates:
            coordinates.remove(closest)
    
    return coordinates

def sum_distances(x, y, coordinates):
    sum = 0
    for c in coordinates:
        sum += abs(x - c[0]) + abs(y - c[1])
    return sum

def part1():
    coordinates = file_input()
    area = {}
    for y in range(0, 400):
        for x in range(0, 400):
            closest = get_closest(x, y, coordinates)
            if closest and closest in area:
                area[closest] += 1
            elif closest:
                area[closest] = 1
    print(area)
    coordinates = remove_infinite(coordinates)

    result = {}
    for k, v in area.items():
        if k in coordinates:
            result[k] = v

    return max(result.values())

def part2():
    coordinates = file_input()
    area = 0
    for y in range(0, 1000):
        for x in range(0, 1000):
            if sum_distances(x, y, coordinates) < 10000:
                area += 1
    return area

print(part2())
    
