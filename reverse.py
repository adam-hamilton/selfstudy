#!/usr/bin/python3.6

def reverse(alist):
    "produces reverse list in place"
    left = 0
    right = len(alist) - 1

    while left < right:
        alist[left], alist[right] = alist[right], alist[left]
        left += 1
        right -= 1
    return alist