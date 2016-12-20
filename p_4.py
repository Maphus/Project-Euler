#!/usr/bin/python

#
#   Project Euler #4
#   Largest palindrome from 2 3 digit numbers
#

def getResult( arg1 , arg2):
    return arg1 * arg2

def isPalindrome( arg1 ):
    if str(arg1) == str(arg1)[::-1]:
        return arg1
    return 0
l = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        k = getResult(i,j)
        k = isPalindrome(k)
        if k != 0:
            if k > l:
                l = k

print(l)
