import re
import time
import sys

def input():
    pattern = re.compile("position=<([ -]*[\d]+),([ -]*[\d]+)> velocity=<([ -]*[\d]+),([ -]*[\d]+)>")
    points = []
    with open('input.txt') as f:
        line = f.readline()
        while line:
            matches = pattern.match(line)
            data = []
            for i in range(0, 4):
                data.append(int(matches.group(i+1).strip()))
            
            points.append(data)
            line = f.readline()
    return points

def output(positions):
    xs = list(map(lambda e: e[0], positions))
    ys = list(map(lambda e: e[1], positions))

    min_x, max_x, min_y, max_y = min(xs), max(xs), min(ys), max(ys)
    if max_x - min_x > 100 and max_y - min_y > 100: return False

    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            if (x, y) in positions:
                sys.stdout.write('# ')
            else:
                sys.stdout.write('. ')
        sys.stdout.write('\n')
    sys.stdout.flush()
    return True

def part1and2():
    points = input()
    count = 1
    while True:
        for p in points:
            p[0] += p[2]
            p[1] += p[3]
        if output(list(map(lambda p: (p[0], p[1]), points))):
            print(count)
            print(count)
            print(count)
            time.sleep(1)
        count += 1