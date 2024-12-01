# Advent of Code 2024
# Day 1

def p1(input):
    left = (int(line.split()[0]) for line in input)
    right = (int(line.split()[1]) for line in input)
    left = sorted(left)
    right = sorted(right)

    total = 0
    for left, right in zip(left, right):
        total += abs(left - right)

    print(f"Part 1 solution: {total}")


def p2(input):
    left = (int(line.split()[0]) for line in input)
    right = (int(line.split()[1]) for line in input)
    right = sorted(right)
    
    counter = {}
    for num in right:
        counter[num] = counter.get(num, 0) + 1
    total = sum(counter[num] * num for num in left if num in counter)

    print(f"Part 2 solution: {total}") 

input = open("input_p1.txt").readlines()

p1(input)
p2(input)
