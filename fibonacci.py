def fib(x):
    if x == 2 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

print (fib (10) )


'''
The Fibonacci series can start from 0 or 1. The base condition can be decided accordingly.
In this case the series considered to be started with 0
'''
