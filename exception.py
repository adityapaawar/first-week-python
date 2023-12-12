'''
try:
    num1 =int(input("enter the num"))
    num2 =int(input("enter the second num"))
    try:
        result=num1/num2
        print("the result is: " , result)
    except ZeroDivisionError:
        print("Error: do not write Zero")

except ValueError:
    print("Error:enter the valid value")
    
'''               
try:
    values = input("Enter two values separated by a space: ")
    val1, val2 = values.split()

    if len(val1) > 6 or len(val2) > 6:
        raise ValueError("Error: Values should not have more than 6")

    print("Value 1:", val1)
    print("Value 2:", val2)

except ValueError:
    print("Error:do not enter num")
