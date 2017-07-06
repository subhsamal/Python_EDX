'''
Problem 4
10.0/10.0 points (graded)
Write a function is_triangular that meets the specification below. A triangular number is a number obtained by the continued summation of integers starting from 1.
For example, 1, 1+2, 1+2+3, 1+2+3+4, etc., corresponding to 1, 3, 6, 10, etc., are triangular numbers.

def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    #YOUR CODE HERE
'''
def is_triangular(k):
    i = 1
    if i == k:
        return True
    elif i+ 2 == k:
        return True
    else:
        sum_ = 3
        i = 3
        while i < k:
            sum_ = sum_ + i
            if sum_ == k:
                return True
            else:
                i = i + 1
                continue
        return False
