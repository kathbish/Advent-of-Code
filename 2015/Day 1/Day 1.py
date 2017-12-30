file = open("Day 1 input", "r")
input = file.read()

def part1(input):
    floor = 0
    for char in input:
        if char == "(":
            floor = floor + 1
        if char == ")":
            floor = floor - 1
    return floor
print(part1(input))

def part2(input):
    floor = 0
    index = 1
    for char in input:
        if char == "(":
            floor = floor + 1
            if floor == -1:
                return index
        if char == ")":
            floor = floor - 1
            if floor == -1:
                return index
        index+=1
print(part2(input))
