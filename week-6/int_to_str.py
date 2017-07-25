'''
A program to convert a given integer to string
'''


def intToStr(i):
    digits = '0123456789'
    if i== 0:
        return '0'
    result = ''
    while i> 0:
        print ("result", result)
        result = digits[i%10] + result              #rightmost digit of integer will be stored in the result and get appended at right
        i = i//10
    return result


string = intToStr(1000203)
#print (type (1000203))
print (string)
#print (type(string))
