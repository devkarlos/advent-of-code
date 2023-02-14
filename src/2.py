# https://adventofcode.com/2022/day/2
from get_data import get_data

data = get_data(2)

"""
A, X - Rock
B, Y - Paper
C, Z - Scissors
"""

# Part 1

def calc_score_for_shape(shape: str) -> int:
    if shape == "X":
        return 1
    elif shape == "Y":
        return 2
    elif shape == "Z":
        return 3
    else:
        return 0

c = 0
for d in data:
    if (d[0] == "A" and d[2] == "X") or (d[0] == "B" and d[2] == "Y") or (d[0] == "C" and d[2] == "Z"):
        c += 3
        c += calc_score_for_shape(d[2])
    # scissors rock
    elif d[0] == "C" and d[2] == "X":
        c += 6
        c += calc_score_for_shape(d[2])
    # paper scissors
    elif d[0] == "B" and d[2] == "Z":
        c += 6
        c += calc_score_for_shape(d[2])
    # rock paper
    elif d[0] == "A" and d[2] == "Y":
        c += 6
        c += calc_score_for_shape(d[2])
    else:
        c+=0
        c += calc_score_for_shape(d[2])

print(f"Part one: {c}")

# Part 2

def get_shape_to_lose(input: str) -> str:
    if input == "A":
        return "Z"
    elif input == "B":
        return "X"
    elif input == "C":
        return "Y"
    else:
        return ""

def get_shape_to_draw(input: str) -> str:
    if input == "A":
        return "X"
    elif input == "B":
        return "Y"
    elif input == "C":
        return "Z"
    else:
        return ""
    
def get_shape_to_win(input: str) -> str:
    if input == "A":
        return "Y"
    elif input == "B":
        return "Z"
    elif input == "C":
        return "X"
    else:
        return ""

c = 0
for d in data:
    # Lose
    if d[2] == "X":
        c += calc_score_for_shape(get_shape_to_lose(d[0]))
    # Draw
    elif d[2] == "Y":
        c += 3
        c += calc_score_for_shape(get_shape_to_draw(d[0]))
    # Win
    elif d[2] == "Z":
        c += 6
        c += calc_score_for_shape(get_shape_to_win(d[0]))
    else:
        print(f"Invalid input: {d}")
    
print(f"Part two: {c}")