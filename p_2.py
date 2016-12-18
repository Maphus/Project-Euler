#!/usr/bin/python

#
#   Project Euler project 2
#   Sum of even Fibonacci numbers up to 4 million
#

max = 4000000 #sets max Fibonacci number to evaluate to
cur_Fib = 1   #current Fibonacci number
pre_Fib = 0   #previous Fibonacci number
nex_Fib = 0
final = 0     #final number of series

while nex_Fib <= max:
    nex_Fib = pre_Fib + cur_Fib
    if nex_Fib % 2 == 0:
        if nex_Fib < max:
             final += nex_Fib

    pre_Fib = cur_Fib
    cur_Fib = nex_Fib

print final