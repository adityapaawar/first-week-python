#program for managing employee records. store employee data and salary and
#calculate the total expenses for all the employees.

#Employee Information
employees=[
    ('Alice', 'E001', 'Manager', 60000),
    ('Bob', 'E002', 'Devloper', 55000),
    ('Charlie','E003',  'Designer', 50000),
    ]
total_expenses=0
#method 1 using unpacking of the tuples
print('using method=unpacking for the tuples-->')
for employee in employees:
    name,e_id,postion,salary=employee
    total_expenses+=salary
print(f"The total expenses for all employee is {total_expenses}")


#method 2 using Indexing
print('2,using method=indexing -->')
for employee in employees:
    total_expenses+=(employee[-1])
print(f"The total expenses for all employee is {total_expenses}")
