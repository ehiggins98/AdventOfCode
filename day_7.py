import re
from string import ascii_uppercase

def input():
    matches = init_matches()
    with open('input.txt') as f:
        line = f.readline()
        pattern = re.compile('Step ([A-Z]) must be finished before step ([A-Z]) can begin.')
        while line != '':
            match = pattern.match(line)
            matches[match.group(2)].append(match.group(1))
            line = f.readline()
    return matches

def init_matches():
    matches = {}
    for c in ascii_uppercase:
        matches[c] = []
    return matches

def clean_matches(completed, matches):
    matches.pop(completed, None)
    
    for k, v in matches.items():
        if completed in v:
            v.remove(completed)
    return matches

def steps_complete(list, complete):
    for c in list:
        if c not in complete:
            return False
    return True

def part1():
    matches = input()
    complete = ''
    ready = []

    while len(matches) > 0:
        for k, v in matches.items():
            if steps_complete(v, complete):
                ready.append(k)
        complete += sorted(ready)[0]
        clean_matches(complete[-1], matches)
        ready = []
    return complete

def part2():
    matches = input()
    initial_length = len(matches)
    complete = ''
    ready = []
    time = 0
    workers = [('', 0), ('', 0), ('', 0), ('', 0), ('', 0)]

    while len(matches) > 0 or len(complete) < initial_length:
        for i in range(len(workers)):
            w = workers[i]
            if not w[0] or ord(w[0]) - 5 + w[1] == time:
                complete += w[0]
                clean_matches(w[0], matches)
                workers[i] = ('', time+1)

        for i in range(len(workers)):
            w = workers[i]
            if not w[0]:
                for k, v in matches.items():
                    if steps_complete(v, complete):
                        ready.append(k)
                if len(ready) > 0:
                    workers[i] = (sorted(ready)[0], time+(time != 0))
                    matches.pop(sorted(ready)[0])
                    ready = []
        time += 1
    return time