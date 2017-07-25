'''
Exercise: genPrimes
Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...'''

def genPrimes( n = 2):
    while True:
        if all (n % i != 0 for i in range (2, n//2+1)):
            yield n
            n += 1
        else:
            n += 1
       # n = n+1


    
