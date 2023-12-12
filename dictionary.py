#write a python script to generate and print a dictionary contains a number
#(between 1 and n) in the form (x,x*x).

n=int (input("input a number"))
d=dict()

for x in range (1,n+1):
    d[x]=x*x

print (d)



dic1={"Name":"Nikita","Year1":"2023"}
dic2={"Year":"2023"}

dic3={}
dic3.update(dic1)
dic3.update(dic2)
print(dic3)



