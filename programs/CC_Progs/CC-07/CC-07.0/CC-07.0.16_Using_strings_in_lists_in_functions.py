#!/usr/bin/python

n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
    result = ""
    for i in words:
        result += i
    return result
print join_strings(n)
