#create a program that accesses elements from a list and handles the exception.

my_list = [1, 2, 3, 4, 5]
print(my_list)
try:
    index=int (input("Enter the index of the element you want to aaccess: "))
    element = my_list[index]
    print("Element at index ",index, "is" ,element)
except IndexError:
    print("Invalid index. please enter a valid index within the range of the list")
        


