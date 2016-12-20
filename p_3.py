#!/usr/bin/python
import math

#
#   Project Euler problem #3
#   Findin largest prime factor of a given number
#   Implemented with function practice
#

def isFactor( arg1 , max ):
    rtrn = 0
    if max % arg1 == 0:
        rtrn = arg1
    return rtrn

def checkPrime( arg1 ):
    i = arg1 / 2
    while i > 1:
        if arg1 % 2 == 0:
            return 0
        if arg1 % i == 0:
            return 0
        i -= 1
    return arg1

result = 3
final = 3
final2 = 0
max = 600851475143
realmax = math.ceil(math.sqrt(max))
while result < realmax:
    final = isFactor( result , max )
    if final != 0:
        final = checkPrime( result )
    if final != 0:
        final2 = final
    result += 1

print(final2)
