# Advent of Code
# Two sum problem
# in Python
# d-toth1

# Read and process input file 
with open("input.txt") as f:
    data = f.read().splitlines()

for i in range(len(data)):
    data[i] = int(data[i])


def two_sum_prod(a, two_sum):
    """
    Given an array 'a', finds the elements
    of 'a' that have a sum equal to two_sum
    and returns their product
    
    """
    sum_dict = {}

    for i in range(len(a)):
        diff = two_sum - a[i]

        if diff in sum_dict:
            return a[i]*diff

        sum_dict[a[i]] = a[i]

    return


def three_sum_prod(a, three_sum):
    """
    Does the same thing as the above
    function, but finds 3 elements in the
    array that sum to the desired value.

    """
    sum_dict = {}

    for i in range(len(a)):
        
        for j in range(i+1, len(a)):
            diff = three_sum - a[i] - a[j]
            
            if diff in sum_dict:
                return a[i]*a[j]*diff
            
            sum_dict[a[j]] = a[j]

    return

# Solution
soln1 = two_sum_prod(data, 2020)
print(soln1)

soln2 = three_sum_prod(data, 2020)
print(soln2)
