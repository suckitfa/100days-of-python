import art
import os
print(art.logo)
os.system("cls")

# what is the first number?
# + - * /
# Pick an operation:
# what's the next number?:
# 3.0 * 5.0 = 15.0
# Type 'y' to continue calculating with 15.0 or type 'n' to start a new calculation

def add(num1,num2):
    return num1 + num2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1/n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

num1 = float(input("What's the first number?:"))
for symbol in operations:
    print(symbol)

should_continue = True
while should_continue:
    operation_symbol = input("Pick an operation from the line above:")
    cal_func = operations[operation_symbol]
    num2 = float(input("What's the next number?:"))
    answer = cal_func(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation") == 'y':
        num1 = answer
    else:
        should_continue = False