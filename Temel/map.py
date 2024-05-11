numbers = [1, 2, 3, 4, 5]


squaredNumbers = list(map(lambda x: x**2, numbers))

# for number in numbers:
#   squaredNumbers.append(number*number)


filteredNumbers = list(filter(lambda x: x>2,numbers))

from functools import reduce
numbersFactorial = reduce(lambda x,y: x*y,numbers)

print(filteredNumbers)
print(squaredNumbers)
print(numbersFactorial)
