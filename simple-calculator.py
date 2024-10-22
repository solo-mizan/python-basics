# simple calculator in python

num1 = float(input("Enter first number: "))
operator = input("Enter a arithmetic operator (+ (-) (*) (/) : ")
num2 = float(input("Enter second number: "))

result = 0

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2

if operator not in ["+", "-", "*", "/"]:
    print(f"{operator} is not a valid operator")
else:
    print(f"Result = {round(result, 2)}")