number1 = float(input())
number2 = float(input())
operation = input()
if operation == "+":
    print(number1 + number2)
elif operation == "-":
    print(number1 - number2)
elif operation == "*":
    print(number1 * number2)
elif operation == "/" and number2 == 0:
    print(888888)
else:
    print(number1 / number1)