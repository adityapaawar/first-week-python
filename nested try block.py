#Write a program of nested try block.

try:
    num1 = int(input("Enter NO. NUM1: "))
    num2 = int(input("Enter NO. NUM2: "))

    try:
        result=num1/num2
        print(result)

    except ZeroDivisionError:
        print("Error: cannot divide by zero!")

except ValurError:
    print("Invaid input")



