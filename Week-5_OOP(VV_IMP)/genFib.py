# -*- coding: utf-8 -*-
"""
Fibonacci number using Generators
6.00.1x - Week 5

"""

def genFib():
    fibn_1 = 1 #fib(n-1)
    fibn_2 = 0 #fib(n-2)
    while True:
        # fib(n) = fib(n-1) + fib(n-2)
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next

fib = genFib()
#val = fib.__next__()
#print (val)
#for n in genFib():
print (next(fib))
print (next(fib))
print (next(fib))
print (next(fib))
print (next(fib))
