#!/usr/bin/python3
# Author: rap7or22
# 12/2/2018
from collections import Counter


def partOne():
    twos = 0
    threes = 0
    file = open('input').read().splitlines()
    for line in file:
        counts = Counter(Counter(line).values())
        if 2 in counts:
            twos+=1
        if 3 in counts:
            threes+=1

    print("Checksum:", twos*threes)

def partTwo():
    file = open('input').read().splitlines()
    for line1 in file:
        for line2 in file:
            difference = [i for i,x in zip(line1,line2) if i == x]
            if len(line1)-len(difference) == 1:
                print("".join(difference))
                return 1
   
def main():
    partOne()
    partTwo()
    exit()

main()
