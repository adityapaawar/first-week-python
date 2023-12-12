#Take a list and filter out positive numbers from the list and print the list in reverse

list2=[]
list1=[1,8,6,-4,-5]
for i in list1:
    if i>=0:
        list2.append(i)
    
        i=len(list2)-1
        while i>=0:
            print(list2[i])
            i-=1
