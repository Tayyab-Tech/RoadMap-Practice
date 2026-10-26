# Statistics Calculator
# Functions:
# Mean
# Median
# Mode
# Maximum
# Minimum
# Range
# Accept any list of numbers.

# import calculater as c

# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))
# symbol = input("Enter +,-,*,/,% to calculate : ")
# while symbol not in "+-*/%":
#     symbol = input("Invalid! Enter +,-,*,/,% : ")
# c.calculate(num1,num2,symbol)

def mean(numbers):
    return sum(numbers) / len(numbers)
def median(numbers):
    numbers = sorted(numbers)
    n = len(numbers)
    if n % 2 == 1:
        return numbers[n // 2]
    else:
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2
def mode(numbers):
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    max_count = max(frequency.values())
    for key, value in frequency.items():
        if value == max_count:
            return key
def maximum_num(numbers):
    return max(numbers)
def minimum_num(numbers):
    return min(numbers)
def range_num(numbers):
    return max(numbers) - min(numbers)
def statistics(numbers):
    print("Mean:", mean(numbers))
    print("Median:", median(numbers))
    print("Mode:", mode(numbers))
    print("Maximum:", maximum_num(numbers))
    print("Minimum:", minimum_num(numbers))
    print("Range:", range_num(numbers))
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
statistics(numbers)