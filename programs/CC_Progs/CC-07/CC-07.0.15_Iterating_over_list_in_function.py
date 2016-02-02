#!/usr/bin/python

n = [3, 5, 7]
def total(numbers):
    result = 0
    for i in range(0, len(numbers)):
        result += numbers[i]
    return result
