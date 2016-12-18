#!/usr/bin/python

#
#   Project Euler #1
#   Find the sum of all the multiples of 3 or 5 below 1000
#   And find their sum
#

final = 3 #accounting for the three
i = 5     #start at 5

while i < 1000:
    if i % 3 == 0:
        final += i
    elif i % 5 == 0:
        final += i
    i += 1

print final
