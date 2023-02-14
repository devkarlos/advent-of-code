# https://adventofcode.com/2022/day/4
from get_data import get_data

data = get_data(4)

# Part 1

temp = []
for d in data:
    d = d.split("-")
    d = " ".join(d).split(",")
    temp.append(d)

supplies = []
for t in temp:
    for n in t:
        supplies.append([int(x) for x in range(int(n.split(" ")[0]), int(n.split(" ")[1]) + 1)])

print(supplies)

c = 0
for i in range(len(supplies) - 1):
    s1 = supplies[i]
    if (i+1)%2 != 0:
        s2 = supplies[i+1]
        if all([s in s1 for s in s2]) or all([s in s2 for s in s1]):
            c+=1

print(f"Part one: {c}")

# Part 2

c = 0
for i in range(len(supplies) - 1):
    s1 = supplies[i]
    if (i+1)%2 != 0:
        s2 = supplies[i+1]
        for s in s1:
            if s in s2:
                c += 1
                break

print(f"Part two: {c}")