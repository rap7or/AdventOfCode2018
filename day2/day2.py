#!/usr/bin/python3
from collections import Counter


def partOne():
    twos = 0
    threes = 0
    file = open('input', 'r')
    for line in file:
        counts = Counter(Counter(line).values())
        if 2 in counts:
            twos+=1
        if 3 in counts:
            threes+=1

    print("Checksum:", twos*threes)

def p1():
    twos = 0
    threes = 0
    file = open('input', 'r')
    for line in file:
        counts = Counter(line).values()
        if 2 in counts:
            twos += 1
        elif 3 in counts:
            threes += 1
    
    print("Checksum:", twos*threes)
def main():
    partOne()
    p1()
    return 1

main()
