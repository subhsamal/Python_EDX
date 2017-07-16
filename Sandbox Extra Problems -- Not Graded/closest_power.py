'''
Implement a function called closest_power that meets the specifications below.

def closest_power(base, num):

    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.

For example,

closest_power(3,12) returns 2
closest_power(4,12) returns 2
closest_power(4,1) returns 0
Paste your entire function, including the definition, in the box below. Do not leave any debugging print statements.

'''
def closest_power(base, num):
    exponent = 0
    smaller = 0
    bigger = 0
    result1 = 0
    result2 = 0
    while base**exponent < num:
        result1 = base ** exponent
        smaller = exponent
        exponent += 1

    if base ** exponent > num:
        result2 = base ** exponent
        bigger = exponent

    if (num - result1) > abs(num - result2):
        return bigger
    else:
        return smaller
