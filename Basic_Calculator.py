number1=int(input("Enter First Input: "))
number2=int(input("Enter Second Input: "))

Operator = input("Enter the type of operator you want to perform with(+,-,*,/,%): ")

result = 0

if Operator == "+":
    result = number1 + number2

elif Operator == "-":
    result = number1 - number2

elif Operator == "*":
    result = number1 * number2

elif Operator == "/":
    result = number1 / number2

elif Operator == "%":
    result = number1 % number2

print(f"The Result is {number1}{Operator}{number2} = {result}")