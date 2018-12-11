import numpy as np

array = np.zeros((300, 300))
serial = 9995

def sum_square(size, x, y):
    return np.sum(array[y-1:y-1+size,x-1:x-1+size])

def part2():
    maxpower = 0
    argmax = None
    for x in range(1, 301):
        for y in range(1, 301):
            id = x + 10
            power = id * y + serial
            power *= id
            number = str(power)
            power = int(number[-3] if len(number) >= 3 else 0)
            power -= 5
            array[y-1][x-1] = power
    for size in range(1, 301):
        if size % 10 == 0:
            print(size)
        for x in range(1, 299):
            for y in range(1, 299):
                power = sum_square(size, x, y)
                if power > maxpower:
                    maxpower = power
                    argmax = (x, y, size)
    return argmax, maxpower

print(part2())
