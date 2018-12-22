#!/usr/bin/python3

def partOne():
    file = open('input').read().splitlines()
    line = file[0]
    oldline = None
    while oldline != line:
        oldline = line
        for i in range(0,26):
            line = line.replace(chr(ord("a") + i) + chr(ord("A") + i),"")
            line = line.replace(chr(ord("A") + i) + chr(ord("a") + i),"")

    return (len(line), line)
def partTwo(bestLine):
    bestLen = len(bestLine)

    for i in range(0,26):
        line = bestLine
        line = line.replace(chr(ord("a") + i),"")
        line = line.replace(chr(ord("A") + i),"")

        old = None
        while old != line:
            old = line
            for x in range(0,26):
                line = line.replace(chr(ord("a") + x) + chr(ord("A") + x),"")
                line = line.replace(chr(ord("A") + x) + chr(ord("a") + x),"")

        if len(line) < bestLen:
            bestLen = len(line)
    return bestLen


def main(): 
    length, line = partOne()
    print("part one:", length)
    print("part two:", partTwo(line))
main()