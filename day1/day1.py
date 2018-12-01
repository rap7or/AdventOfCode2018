#!/usr/bin/python3

import itertools

def partOne():
    data = open("./input", 'r')
    total = 0
    for line in data:
        line = line.strip()
        if line[0] == '+':
            total += int(line[1:])
        if line[0] == '-':
            total -= int(line[1:])

    data.close()
    print("fequency:", total)

def partTwo():
    data = [int(i) for i in open("input").readlines()]
    freq = 0
    seen = {0}
    for num in itertools.cycle(data):
        freq += num
        if freq in seen:
            print("first repeated frequency:", freq)
            break
        seen.add(freq)
def main():
    partOne()
    partTwo()

main()