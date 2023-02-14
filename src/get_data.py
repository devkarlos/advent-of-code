import os

def get_data(day: int) -> list:
    file = open(f"{os.getcwd()}/input/{day}.txt", "r")
    data = []
    for line in file:
        data.append(line.rstrip("\n"))
    return data