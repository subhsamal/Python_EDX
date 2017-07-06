'''
Problem 7
20.0/20.0 points (graded)
Write a function called dict_invert that takes in a dictionary with immutable values and returns the inverse of the dictionary. The inverse of a dictionary d is another dictionary whose keys are the unique dictionary values in d. The value for a key in the inverse dictionary is a sorted list (increasing order) of all keys in d that have the same value in d.

Here are two examples:

If d = {1:10, 2:20, 3:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3]}
If d = {1:10, 2:20, 3:30, 4:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3, 4]}
If d = {4:True, 2:True, 0:True} then dict_invert(d) returns {True: [0, 2, 4]}
def dict_invert(d):

    d: dict
    Returns an inverted dictionary according to the instructions above
    '''

# Paste your function here
def dict_invert(d):
    #inv_d = {v: k for k, v in d.items()}
    inv_d = {}
    for k,v in sorted(d.items()):
        inv_d.setdefault(v,[]).append(k)
    return inv_d
