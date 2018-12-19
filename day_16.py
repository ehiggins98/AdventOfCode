import copy
import ast

def input():
    instructions = []
    with open('input.txt') as f:
        before = f.readline()
        while before:
            instr = f.readline()
            after = f.readline()
            f.readline()

            before = before[before.index(' ') + 1:-1]
            after = after[after.index(' ') + 2:-1]
            instr = instr[:-1]
            instructions.append((before, instr, after))
            before = f.readline()
    return instructions

def program():
    instructions = []
    with open('program.txt') as f:
        line = f.readline()[:-1]
        while line:
            instructions.append(list(map(lambda x: int(x), line.split(' '))))
            line = f.readline()[:-1]
    return instructions

class Ops:

    @staticmethod
    def to_val(a, b, r, registers):
        a = registers[a]
        if r:
            b = registers[b]
        return a, b

    @staticmethod
    def add(a, b, c, r, registers):
        a, b = Ops.to_val(a, b, r, registers)
        result = copy.deepcopy(registers)
        result[c] = a + b
        return result

    @staticmethod
    def mul(a, b, c, r, registers):
        a, b = Ops.to_val(a, b, r, registers)
        result = copy.deepcopy(registers)
        result[c] = a * b
        return result

    @staticmethod
    def and_f(a, b, c, r, registers):
        a, b = Ops.to_val(a, b, r, registers)
        result = copy.deepcopy(registers)
        result[c] = a & b
        return result

    @staticmethod
    def or_f(a, b, c, r, registers):
        a, b = Ops.to_val(a, b, r, registers)
        result = copy.deepcopy(registers)
        result[c] = a | b
        return result

    @staticmethod
    def set_f(a, b, c, r, registers):
        _, a = Ops.to_val(0, a, r, registers)
        result = copy.deepcopy(registers)
        result[c] = a
        return result

    @staticmethod
    def greater(a, b, c, r1, r2, registers):
        _, a = Ops.to_val(0, a, r1, registers)
        _, b = Ops.to_val(0, b, r2, registers)

        result = copy.deepcopy(registers)
        result[c] = int(a > b)
        return result

    @staticmethod
    def equal(a, b, c, r1, r2, registers):
        _, a = Ops.to_val(0, a, r1, registers)
        _, b = Ops.to_val(0, b, r2, registers)

        result = copy.deepcopy(registers)
        result[c] = int(a == b)
        return result

def greater(a, b, c, r1, r2, registers):
    print(a, b, c, r1, r2, registers)
    _, a = Ops.to_val(b, a, r1, registers)
    _, b = Ops.to_val(a, b, r2, registers)

    result = copy.deepcopy(registers)
    result[c] = int(a > b)
    print(a, b, result, '\n')
    return result

def equal(a, b, c, r1, r2, registers):
    _, a = Ops.to_val(b, a, r1, registers)
    _, b = Ops.to_val(a, b, r2, registers)

    result = copy.deepcopy(registers)
    result[c] = int(a == b)
    return result

def part1():
    instructions = input()

    singles = [Ops.add, Ops.mul, Ops.and_f, Ops.or_f, Ops.set_f]
    doubles = [Ops.greater, Ops.equal]
    total = 0

    for e in instructions:
        before, instr, after = e
        before = ast.literal_eval(before)
        after = ast.literal_eval(after)
        instr = list(map(lambda e: int(e), instr.split(' ')))
        possible = 0
        for s in singles:
            for r in [True, False]:
                result = s(instr[1], instr[2], instr[3], r, before)
                if result == after:
                    possible += 1
        for d in doubles:
            for r1 in [True, False]:
                for r2 in [True, False]:
                    result = d(instr[1], instr[2], instr[3], r1, r2, before)
                    if result == after:
                        possible += 1

        if possible >= 3:
            total += 1
        return total

def part2():
    instructions = input()

    singles = {Ops.add, Ops.mul, Ops.and_f, Ops.or_f, Ops.set_f}
    doubles = {Ops.greater, Ops.equal}
    tentative = {}

    for s in singles:
        for r in {True, False}:
            tentative[(s, r)] = list(range(0, 16))
    for d in doubles:
        for r1 in {True, False}:
            for r2 in {True, False}:
                tentative[(d, r1, r2)] = list(range(0, 16))

    for e in instructions:
        before, instr, after = e
        before = ast.literal_eval(before)
        after = ast.literal_eval(after)
        instr = list(map(lambda e: int(e), instr.split(' ')))

        for s in singles:
            for r in {True, False}:
                result = s(instr[1], instr[2], instr[3], r, before)
                if result != after and instr[0] in tentative[(s, r)]:
                    tentative[(s, r)].remove(instr[0])
        for d in doubles:
            for r1 in {True, False}:
                for r2 in {True, False}:
                    result = d(instr[1], instr[2], instr[3], r1, r2, before)
                    if result != after and instr[0] in tentative[(d, r1, r2)]:
                        tentative[(d, r1, r2)].remove(instr[0])

    mappings = {}
    while len(mappings) < 16:
        for k, v in tentative.items():
            if k not in mappings.values() and len(v) == 1:
                mappings[v[0]] = k
                for k1, v1 in tentative.items():
                    if v[0] in v1 and k1 != k: 
                        v1.remove(v[0])
    
    registers = [0] * 5
    for instr in program():
        func = mappings[instr[0]]
        if len(func) == 2:
            registers = func[0](instr[1], instr[2], instr[3], func[1], registers)
        elif len(func) == 3:
            registers = func[0](instr[1], instr[2], instr[3], func[1], func[2], registers)
        
    return registers
