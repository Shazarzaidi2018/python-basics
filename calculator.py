a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
op = input("Enter an operator (+, -, *, /, %): ")

if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "%":
    result = a % b
elif op == "/":
    if b != 0:
        result = a / b
    else:
        print("Cannot divide by zero")
        exit()
else:
    print("Invalid operator")
    exit()

print("Result:", result)
