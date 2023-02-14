# https://adventofcode.com/2022/day/3
import string
from get_data import get_data

data = get_data(3)

# Part 1

alphabet = list(string.ascii_letters)

def find_duplicate(string1: str, string2: str) -> str:
    for s1 in string1:
        if s1 in string2:
            return s1
        
    for s2 in string2:
        if s2 in string1:
            return s2
        
def get_priority_sum(items: list) -> int:
    c = 0
    for i in items:
        c += alphabet.index(i) + 1
    return c

temp = []
for d in data:
    if len(d)%2 == 0:
        temp.append(find_duplicate(d[0:int(len(d)/2)], d[int(len(d)/2):int(len(d))]))
    else:
        print(f"Input error: {d}")

print(f"Part one: {get_priority_sum(temp)}")

# Part 2

def find_duplicate(string1: str, string2: str, string3: str) -> str:
    for s1 in string1:
        if s1 in string2 and s1 in string3:
            return s1
        
    for s2 in string2:
        if s2 in string1 and s2 in string3:
            return s2
        
    for s3 in string3:
        if s3 in string1 and s3 in string2:
            return s3
        
groups = []
temp = []

for d in data:
    if len(temp) < 2:
        temp.append(d)
    else:
        temp.append(d)
        groups.append(temp)
        temp = []

c = 0
for g in groups:
    c += get_priority_sum(find_duplicate(g[0], g[1], g[2]))

print(f"Part two: {c}")