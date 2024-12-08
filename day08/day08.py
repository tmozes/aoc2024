# Advent of Code 2024
# Day 8

from collections import defaultdict
from itertools import combinations

input = open("input_p1.txt").readlines()
board = [list(line.strip()) for line in input]

def on_board(r, c):
    return 0 <= r < len(board) and 0 <= c < len(board[r])

def print_board(board):
    for r in range(len(board)):
        for c in range(len(board[r])):
            print(board[r][c], end="")
        print()

letters = defaultdict(list)
unique_coords_p1 = set()
unique_coords_p2 = set()

for r in range(len(board)):
    for c in range(len(board[r])):
        letter = board[r][c]
        if letter != ".":
            letters[letter].append((r, c))
        
for letter, coordiantes in letters.items():
    coordinate_pairs = list(combinations(coordiantes, 2))
    for pair in coordinate_pairs:
        dr = pair[1][0] - pair[0][0]
        dc = pair[1][1] - pair[0][1]

        # 1st part
        n1r = pair[0][0] - dr
        n1c = pair[0][1] - dc

        n2r = pair[1][0] + dr
        n2c = pair[1][1] + dc 
        
        if on_board(n1r, n1c):
           unique_coords_p1.add((n1r, n1c))
        if on_board(n2r, n2c):
            unique_coords_p1.add((n2r, n2c))

        # 2nd part
        # Going forward
        ar =pair[0][0]
        ac =pair[0][1]
        while on_board(ar, ac):
            unique_coords_p2.add((ar, ac))
            ar += dr
            ac += dc

        # Going backward
        ar =pair[0][0]
        ac =pair[0][1]
        while on_board(ar, ac):
            unique_coords_p2.add((ar, ac))
            ar -= dr
            ac -= dc

#print_board(board)
print(f"Part 1 solution: unique coordinates: {len(unique_coords_p1)}")
print(f"Part 2 solution: unique coordinates: {len(unique_coords_p2)}")