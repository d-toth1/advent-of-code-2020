# Advent of Code Day 3
# Ski Slope
# d-toth1

from functools import reduce

with open("input.rtf") as f:
    data = f.read().splitlines()

for i in range(len(data)):
    data[i] = data[i][:-1]

def find_trees(data, x_incr, y_incr):
    """ Finds the number of 
    #s in an infinite grid by 
    incrementing x and y by some
    values.
    
    """
    length = len(data)
    width = len(data[0])
    x = 0
    y = 0
    trees = 0
    
    while y < length:
        row = data[y]
        
        # Use modulo to repeat
        # row in grid 
        pos = row[x % width]
        
        if pos == "#":
            trees += 1
            
        x += x_incr
        y += y_incr
        
    return trees

# Part I
print(find_trees(data, 3, 1))

# Part II
xs = [1,3,5,7,1]
ys = [1,1,1,1,2]
trees = [find_trees(data, xs[i], ys[i]) for i in range(5)]
print(reduce(lambda x,y: x*y, trees))
