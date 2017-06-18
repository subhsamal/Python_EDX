#Program to convert decimal number (both positive and negative to binary)

result = ''
num = int (input ("Enter the number to calculate binary: "))
if num < 0:
    isNeg = True
    num = abs(num)
result = ''
while num > 0:
    result = str (num%2) + result
    num = num // 2
if isNeg == True:
    print ("result = -", result)
else:
    print ("result = ", result)
