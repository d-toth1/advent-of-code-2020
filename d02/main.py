# Advent of Code Day 2
# Password Philosophy
# via Python
# d-toth1

def parse_line1(l):
    """ Parses a line of text
    to determine the min/max number
    of times a specific character
    is allowed in the message.

    """
    col_idx = l.index(':')
    char = l[col_idx - 1]
    min_max = l[:col_idx - 2]
    min_max = list(map(int, min_max.split('-')))
    msg = l[col_idx + 2:]

    if min_max[0] <= msg.count(char) <= min_max[1]:
        return 1
    
    else:
        return 0

def parse_line2(l):
    """ Parses a line of text
    to determine if the specific
    character appears exactly at one
    of the two desired indices.

    """
    col_idx = l.index(':')
    char = l[col_idx - 1]
    idxs = l[:col_idx - 2]
    idxs = list(map(int, idxs.split('-')))
    p1 = idxs[0] - 1
    p2 = idxs[1] - 1
    msg = l[col_idx + 2:]

    cond1 = msg[p1] == char
    cond2 = msg[p2] == char

    # XOR
    if (cond1 and not cond2) or (not cond1 and cond2):
        return 1
    
    else:
        return 0
    
# Counter for correct passwords
correct_pwds1 = 0
correct_pwds2 = 0

# Parse the whole file 
with open("input.txt") as f:
    lines = f.read().splitlines()

    for l in lines:
        correct_pwds1 += parse_line1(l)
        correct_pwds2 += parse_line2(l)


print("Number of correct passwords in v1: ", correct_pwds1)
print("Number of correct passwords in v2: ", correct_pwds2)





  
    
    
