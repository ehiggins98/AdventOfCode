import re
import numpy as np

matrix = np.zeros((1000, 1000))

def input(processor, result):
    with open('input.txt') as f:
        line = f.readline()
        while line != '':
            data = re.split(" ?[#@,:x\n] ?", line)[1:-1]

            processor(data)

            line = f.readline()
    result()
def part1(data):
    for x in range(int(data[1]), int(data[1])+int(data[3])):
        for y in range(int(data[2]), int(data[2])+int(data[4])):
            matrix[y][x] += 1

def output1():
    print(len(matrix[matrix > 1]))

def part2(data):
    overlapping = False
    for x in range(int(data[1]), int(data[1])+int(data[3])):
        for y in range(int(data[2]), int(data[2])+int(data[4])):
            if matrix[y][x] > 0:
                matrix[matrix == matrix[y][x]] = -1
                overlapping = True
            elif matrix[y][x] == 0:
                matrix[y][x] = data[0]
            elif matrix[y][x] == -1:
                overlapping = True
                matrix[y][x] = data[0]
    if overlapping: matrix[matrix == int(data[0])] = -1

def output2():
    print(matrix[matrix > 0][0])