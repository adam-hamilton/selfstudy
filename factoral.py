#!/usr/bin/python

def fact(x):
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result
print(fact(4))
