#Calculator by using if else

a=float(input("enter the first number"))
b=float(input("enter the second"))
c=input("enter the operator")

if c == '+':
    result = a + b
    print(result)
elif c == '*':
    result = a * b
    print(result)
elif c == "/":
    result = a / b
    print(result)
elif c == "-":
    result = a - b
    print(result)
elif c == "//":
    result = a // b
    print(result)
elif c == "**":
    result = a ** b
    print(result)
elif c == "%":
    result = a % b
    print(result)    
else:
    print("operator is not valid")

#Simple calculator    
    
a=45
b=5
print(a + b)
print(a - b)
print(a / b)
print(a * b)
print(a // b)
print(a % b)
print(a ** b)

#Calculator by uing Match case

a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=input("enter the operator(+ - / * // ** %): ")

match c:
    case '+':
        print(a + b)
    case '-':
        print(a - b)
    case '*':
        print(a * b)
    case '/':
        print(a / b)
    case '**':
        print(a ** b)
    case '//':
        print(a // b)
    case '%':
        print(a % b)
    case _:
        print("your operator is wrong")
