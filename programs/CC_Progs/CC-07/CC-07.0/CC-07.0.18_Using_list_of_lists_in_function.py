#!/usr/bin/python

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(x):
    result = []
    for i in x:
        for j in i:
            result.append(j)
    return result
print flatten(n)
