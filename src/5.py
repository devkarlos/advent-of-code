# https://adventofcode.com/2022/day/5
from get_data import get_data

data = get_data(5)

# Part 1

cargo = []
instructions = []

s = 0
for d in data:
    if not d:
        s = 1
    if s == 0:
        cargo.append(d)
    else:
        instructions.append(d)
    
instructions.remove("")

print(cargo)
print(instructions)

#print(f"Part one: {c}")