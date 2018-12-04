#!/usr/bin/python3
import numpy

def partOne():
    file = open('input').read().splitlines()
    values= []
    canvas = numpy.zeros((1000,1000))
    
    for line in file:
        num = int(line.split(' ')[0][1:])
        x,y = int(line.split(' ')[2].split(',')[0]), int(line.split(' ')[2].split(',')[1].split(':')[0])
        w,h = int(line.split(' ')[3].split('x')[0]), int(line.split(' ')[3].split('x')[1])
        values.append([num, x, y, w, h])
    for i, x, y, w, h in values:
        canvas[x:x+w, y:y+h] += 1
    
    print(numpy.sum(canvas>1))

def PartTwo():

    file = open('input').read().splitlines()
    values= []
    canvas = numpy.zeros((1000,1000))
    
    for line in file:
        num = int(line.split(' ')[0][1:])
        x,y = int(line.split(' ')[2].split(',')[0]), int(line.split(' ')[2].split(',')[1].split(':')[0])
        w,h = int(line.split(' ')[3].split('x')[0]), int(line.split(' ')[3].split('x')[1])
        values.append([num, x, y, w, h])
    
    for i, x, y, w, h in values:
        canvas[x:x+w, y:y+h] += 1

    for i, x, y, w, h in values:
        if numpy.all(canvas[x:x+w, y:y+h] == 1):
            print(i)
            break


def main():
    partOne()
    PartTwo()
    

main()
