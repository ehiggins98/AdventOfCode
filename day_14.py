"""

"""
def part1():
    input = 440231
    elves = [0, 1]
    recipes = [3, 7]

    while len(recipes) < input + 10:
        sum = recipes[elves[0]] + recipes[elves[1]]
        recipes += list(map(lambda x: int(x), str(sum)))

        for i, e in enumerate(elves):
            increment = recipes[e] + 1
            elves[i] = (e + increment) % len(recipes)

    if len(recipes) > input+10: recipes = recipes[:input+10]

    print(''.join(list(map(lambda x: str(x), recipes[-10:]))))

def part2():
    input = list(map(lambda x: int(x), list('440231')))
    elves = [0, 1]
    recipes = [3, 7]

    while recipes[-len(input)-1:-1] != input and recipes[-len(input):] != input:
        sum = recipes[elves[0]] + recipes[elves[1]]
        recipes += list(map(lambda x: int(x), str(sum)))

        for i, e in enumerate(elves):
            increment = recipes[e] + 1
            elves[i] = (e + increment) % len(recipes)
    if recipes[-len(input)-1:-1]:
        print(len(recipes) - len(input) - 1)
    else:
        print(len(recipes) - len(input))