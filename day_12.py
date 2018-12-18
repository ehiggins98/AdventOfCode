import copy
import numpy as np

def input():
    state = None
    rules = {}
    with open('input.txt') as f:
        line = f.readline()
        state = line[15:]
        f.readline() # blank line
        line = f.readline()
        while line:
            rules[line[:5]] = line[-2]
            line = f.readline()
    return state[:-1], rules

def next_gen(state, rules):
    next = set()
    for e in state:
        for i in range(e-3, e+4):
            str = ''.join([('#' if i+j in state else '.') for j in range(-2, 3)])
            if str in rules and rules[str] == '#':
                next.add(i)
    return next

def sum_plants(state):
    return np.sum(list(state))

def part1():
    state, rules = input()
    state = set([i for i in range(len(state)) if state[i] == '#'])
    for i in range(20):
        state = next_gen(state, rules)
    return sum_plants(state)

def part2():
    state, rules = input()
    state = set([i for i in range(len(state)) if state[i] == '#'])

    for i in range(97):
        state = next_gen(state, rules)
    return sum_plants(state) + (50000000000 - 97) * 40
