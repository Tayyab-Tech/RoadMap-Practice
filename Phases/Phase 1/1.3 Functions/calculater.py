def add(a,b):
    return a+b
def minus(a,b):
    return a-b
def mul(a,b):
    return a*b
def divi(a,b):
    return a/b
def mod(a,b):
    return a%b
def calculate(a,b,symbol):
    if symbol == '+':
        print(add(a,b))
    elif symbol == '-':
        print(minus(a,b))
    elif symbol == '*':
        print(mul(a,b))
    elif symbol == '/':
        print(divi(a,b))
    elif symbol == '%':
        print(mod(a,b))
    

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
symbol = input("Enter +,-,*,/,% to calculate : ")
while symbol not in "+-*/%":
    symbol = input("Invalid! Enter +,-,*,/,% : ")

calculate(num1,num2,symbol)
