#Multiply numbers in a list using function

def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

my_list = [2, 3, 4, 5]
result = multiply_list(my_list)
print(result)

