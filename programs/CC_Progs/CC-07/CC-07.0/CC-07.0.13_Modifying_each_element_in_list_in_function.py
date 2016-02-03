#!/usr/bin/python

n = [3, 5, 7]
#for i in range(0, len(n)):
#    n[i] = n[i] * 2
# Don't forget to return your new list!
def double_list(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x
print double_list(n)
