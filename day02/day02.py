# Advent of Code 2024
# Day 2

def is_valid(numbers):
    diffs = [next-current for current, next in zip(numbers, numbers[1:])]
    return all(1 <= x <= 3 for x in diffs) or all(-1>= x >= -3 for x in diffs)


def p1(input):
    total_valid = 0
    for line in input:
        numbers = [int(x) for x in line.split()]
        if is_valid(numbers):
            total_valid += 1

    print(f"Part 1 solution: Total valid: {total_valid}")


def p2(input):
    total_valid = 0
    for line in input:
        numbers = [int(x) for x in line.split()]
        i = 0
        if is_valid(numbers):
            total_valid += 1
        else:
            while i < len(numbers):
                new_numbers = [x for n, x in enumerate(numbers) if i != n]
                if is_valid(new_numbers):
                    total_valid += 1
                    break
                i += 1

    print(f"Part 2 solution: Total valid: {total_valid}")

input = open("input_p1.txt").readlines()

p1(input)
p2(input)
