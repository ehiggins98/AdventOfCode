import numpy as np

class Node:
    def __init__(self, metadata, children):
        self.n_metadata = metadata
        self.n_children = children
        self.children = []
        self.metadata = []
    def add_child(self, node):
        self.children.append(node)
    def add_metadata(self, metadata):
        self.metadata.append(metadata)

def input():
    with open('input.txt') as f:
        return list(map(lambda x: int(x), f.readline()[:-1].split(' ')))

def read_node(current, data):
    n_children, n_metadata = data[:2]
    del data[:2]
    temp = Node(n_metadata, n_children)
    if current != None:
        current.add_child(temp)

    for _ in range(n_children):
        read_node(temp, data)
    
    for e in data[:n_metadata]:
        temp.add_metadata(e)
    del data[:n_metadata]

    return temp

def sum_metadata(current):
    sum = np.sum(current.metadata)
    
    for e in current.children:
        sum += sum_metadata(e)
    return sum

def compute_value(current):
    if current.n_children == 0:
        return np.sum(current.metadata)
    else:
        sum = 0
        for e in current.metadata:
            if e <= len(current.children):
                sum += compute_value(current.children[e-1])
    return sum

def part1():
    data = input()
    root = read_node(None, data)
    return sum_metadata(root)

def part2():
    data = input()
    root = read_node(None, data)
    return compute_value(root)