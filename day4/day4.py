#!/usr/bin/python
import collections
def organizeInput():
    file = open('input').read().splitlines()
    status= []
    for line in file:
        status.append(line)
    status.sort()
    return status

def partOne(input):
    guards = collections.defaultdict(int)
    g2 =  collections.defaultdict(int)
    asleep = 0
    awake = 0
    for line in input:
        if "begins shift" in line:
            guardNum = int(line.split()[3][1:])
            asleep = 0
        if "falls asleep" in line:
            asleep = int(line.split()[1][:-1].split(":")[1])
        if "wakes up" in line:
            awake =int(line.split()[1][:-1].split(":")[1])
            for i in range (asleep, awake):
                guards[guardNum] += 1
                g2[(guardNum, i)] += 1

    print(guards)
    maxVal = 0
    guard = 0
    maxMin = 0

    for k,v in g2.items():
        if g2[k] > maxMin:
            maxMin = v
    for k,v in guards.items():
        if guards[k] > maxVal:
            maxVal = v
            guard = k
    print(maxMin)
    print(guard)
    print(maxMin * guard)

def main():
    organized = organizeInput()
    partOne(organized)


main()