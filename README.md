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

Part two was a simple checksum solution, where the solution was the number of box ID's 
with two repeating letters in it multiplied with the number of box ID's with three 
repeating letters in it. Pretty simple to loop through the input and tally the repeating 
letters with the Counter function from the collections library.

Part two was to find the two boxes that differed by only one letter that was the same
place in both ID's. I looped through and compared each ID to every other ID using the
zip function and comparing with the ID I’m checking against.
