#write a pyhton to multiply all the items in a dictionary.

dict = {'data':100,'data2':54,'data3':247}

print(dict)
result=1
for value in dict.values():
    result*=value
print("The multiplication  of all the items in the dictionary is",result)
