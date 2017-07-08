def normalize(numbers):
    max_number = max(numbers)
    for i in range(len(numbers)):
        numbers[i] /= float(max_number)
    return numbers




try:
      normalize([0, 0, 0])
except ZeroDivisionError:
      print('Invalid maximum element')
