# AdventOfCode2018

These are my solutions for the advent of code 2018 https://adventofcode.com/2018

My goal is to *try* and solve each one the day they come out, and document each day here.

# Day 1

Part one was a simple file iteration with some int values that represent frequencies,
and the goal was to find the final frequency. I used python3 and summed up the lines
in the file. Pretty straightforward. End result ended up being 420 _heh_.

Part two was to find the first frequency that was repeated. The caveat was that the 
input could be looped more than once. Answer came to be 227

# Day 2

Part ome was a simple checksum solution, where the solution was the number of box ID's 
with two repeating letters in it multiplied with the number of box ID's with three 
repeating letters in it. Pretty simple to loop through the input and tally the repeating 
letters with the Counter function from the collections library.

Part two was to find the two boxes that differed by only one letter that was the same
place in both ID's. I looped through and compared each ID to every other ID using the
zip function and comparing with the ID I’m checking against.

# Day 3

Today’s task was to map out how each elf chose to lay out possible cutouts in a 1000x1000
sheet. Each possible cutout was given by their distance from the left and top edge, and 
how long each section was. The disgusting file parsing is 100% chalked up to my lack of 
regex knowledge, and resulting in the abomination that is the series of splits that I did
to get each value. Answer was 121163.

My first attempt was to manually tally up each square inch in the fabric and parse through 
each section and tally up how many squared were claimed greater than 1 time. After fumbling 
through this for a bit, I decided that there had to be an array library that did all of this 
for me. In my searching, I came across numpy which had everything I needed. The sum function 
takes an array, and a boolean to check, and return the number of cells that meet the requirement.

Part two was also easily solved by a numpy function: all, which returns true for cells that meet
the given boolean. Once the proposed single section that was only claimed once was found, all was 
needed was the corresponding ID. Answer was 943.

