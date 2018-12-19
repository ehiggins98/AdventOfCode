import copy

def input():
    instructions = []
    with open('input.txt') as f:
        ip = f.readline()[:-1].split(' ')[1]

        line = f.readline()[:-1]
        while line:
            instructions.append(line.split(' '))
            line = f.readline()[:-1]
    return int(ip), instructions

def to_val(a, b, r, registers):
    a = registers[a]
    if r:
        b = registers[b]
    return a, b

def part1():
    ip = 0
    ip_reg, instructions = input()
    memory = [1, 0, 0, 0, 0, 0]
    i = 0
    while ip >= 0 and ip < len(instructions):
        memory[ip_reg] = ip
    
        instr = instructions[ip]
        print(instr, memory)
        name = instr[0][:-1] if instr[0][:2] not in ['eq', 'gt'] else instr[0][:-2]
        name += '_f' if name in ['set', 'or', 'and'] else ''
        
        if name == 'eq': name = 'equal'
        if name == 'gt': name = 'greater'

        func = getattr(Ops, name)
        if name in ['greater', 'equal']:
            r1, r2 = instr[0][-2:]
            memory = func(int(instr[1]), int(instr[2]), int(instr[3]), r1 == 'r', r2 == 'r', memory)
        else:
            r1 = instr[0][-1]
            memory = func(int(instr[1]), int(instr[2]), int(instr[3]), r1 == 'r', memory)
        
        ip = memory[ip_reg] + 1
        i += 1
    return memory

def part2():
    total = 10551394
    sum = 0
    for i in range(1, 10551395):
        if total % i == 0:
            sum += i
    print(sum)

class Ops:

    @staticmethod
    def add(a, b, c, r, registers):
        a, b = to_val(a, b, r, registers)
        result = copy.deepcopy(registers)
        result[c] = a + b
        return result

    @staticmethod
    def mul(a, b, c, r, registers):
        a, b = to_val(a, b, r, registers)
        result = copy.deepcopy(registers)
        result[c] = a * b
        return result

    @staticmethod
    def and_f(a, b, c, r, registers):
        a, b = to_val(a, b, r, registers)
        result = copy.deepcopy(registers)
        result[c] = a & b
        return result

    @staticmethod
    def or_f(a, b, c, r, registers):
        a, b = to_val(a, b, r, registers)
        result = copy.deepcopy(registers)
        result[c] = a | b
        return result

    @staticmethod
    def set_f(a, b, c, r, registers):
        _, a = to_val(0, a, r, registers)
        result = copy.deepcopy(registers)
        result[c] = a
        return result

    @staticmethod
    def greater(a, b, c, r1, r2, registers):
        _, a = to_val(0, a, r1, registers)
        _, b = to_val(0, b, r2, registers)

        result = copy.deepcopy(registers)
        result[c] = int(a > b)
        return result

    @staticmethod
    def equal(a, b, c, r1, r2, registers):
        _, a = to_val(0, a, r1, registers)
        _, b = to_val(0, b, r2, registers)

        result = copy.deepcopy(registers)
        result[c] = int(a == b)
        return result