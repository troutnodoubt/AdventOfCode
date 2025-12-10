
fname='/home/mark/Documents/git/AdventOfCode/2025/input_day10.txt'
fname='/home/mark/Documents/git/AdventOfCode/2025/example_day10.txt'

with open(fname) as fp: data = fp.read().splitlines()

# no idea how to do this one
idea1: find the button closest to the next state and press it. But how to be sure that it's optimal? I think this will give
a sequence that lights things up, just not sure if it's optimal
idea2: run through all possible sequences and count them up. But how to do repeat button presses? Will find best sequences 
assuming each button is only needed once. No way that's the right approach

Idea1 is probably the way to go.

Think on this one some more, clean up the last few days in the meantime
