# Advent of Code 2024
# Day 4

def letter(i,j):
    return board[i][j] if i in range(len(board)) and j in range(len(board[0])) else  None

def p1():
    directions = [
        (-1, 0),  # Left
        (1, 0),   # Right
        (0, -1),  # Up
        (0, 1),   # Down
        (-1, -1), # Left Up
        (-1, 1),  # Right Up
        (1, -1),  # Left Down
        (1, 1)    # Right Down
    ]
    
    valid_paths = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            for di, dj in directions:
                if letter(i, j) == 'X' and letter(i + di, j + dj) == 'M' and letter(i+2*di, j+2*dj) == 'A' and letter(i+3*di, j+3*dj) == 'S':
                    valid_paths += 1
    return valid_paths

def p2():
    valid_paths = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (
                (letter(i, j) == 'A' and 
                    ((letter(i-1, j-1) == 'M' and letter(i+1, j+1) == 'S') or 
                    (letter(i-1, j-1) == 'S' and letter(i+1, j+1) == 'M'))) 
                and
                (letter(i, j) == 'A' and 

                    ((letter(i-1, j+1) == 'M' and letter(i+1, j-1) == 'S') or 
                    (letter(i-1, j+1) == 'S' and letter(i+1, j-1) == 'M'))) 
            ):
                valid_paths += 1
    return valid_paths


board = [line.strip() for line in open("input_p1.txt")]
print(f"Part 1 solution: {p1()}")
print(f"Part 2 solution: {p2()}")