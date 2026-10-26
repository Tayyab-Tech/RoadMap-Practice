# Debug a program that calculates the average of a list incorrectly.
numbers = [10, 20, 30, 40, 50]
average = sum(numbers) / (len(numbers) - 1)
print("Average:", average)
# formula of average is wrong. correct is sum/length 
# correct code is :-
average = sum(numbers) / (len(numbers))
print("Average:", average)





# Fix a loop that runs forever.
i = 1
# while i <= 5:
#     print(i)
# while condition always true because i never increment 
# correct code is :-
while i <= 5:
    print(i)
    i += 1

# Debug a function that returns incorrect factorial values.
def factorial(n):
    result = 0
    # result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial(5))
# result value is 0 which makes all value 0 
# update the result value from 0 to 1 





# Find the logical error in a program that calculates simple interest.
principal = 1000
rate = 5
time = 2
interest = principal * rate * time
print("Simple Interest:", interest)
# formula of interest is wrong so logical bug occurs 
# correct formula is 
interest = (principal * rate * time) / 100





# Use assert to verify that an input number is positive.
try:
    number = int(input("Enter a positive number: "))
    assert number > 0, "Number must be positive."
    print("Valid Number:", number)
except AssertionError as e:
    print(e)