# https://adventofcode.com/2022/day/1
from get_data import get_data

data = get_data(1)

# Part 1

c_sum = []
c = 0

for calories in data:
    if calories:
        c += int(calories)
    elif calories and calories == data[-1]:
        c += int(calories)
        c_sum.append(c)
    else:
        c_sum.append(c)
        c = 0

print(f"Part one: {max(c_sum)}")

# Part 2

maxs = []
maxs.append(max(c_sum))
c_sum.remove(max(c_sum))

maxs.append(max(c_sum))
c_sum.remove(max(c_sum))

maxs.append(max(c_sum))
c_sum.remove(max(c_sum))

print(f"Part two: {sum(maxs)}")