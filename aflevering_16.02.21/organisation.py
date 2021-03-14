'''
Model an organisation of employees, management and board of directors in 3 sets.

Board of directors: Benny, Hans, Tine, Mille, Torben, Troels, Søren
Management: Tine, Trunte, Rane
Employees: Niels, Anna, Tine, Ole, Trunte, Bent, Rane, Allan, Stine, Claus, James, Lars

who in the board of directors is not an employee?
who in the board of directors is also an employee?
how many of the management is also member of the board?
All members of the managent also an employee?
All members of the management also in the board?
Who is an employee, member of the management, and a member of the board?
Who of the employee is neither a memeber or the board or management?

'''

directors = ["Benny", "Hans", "Tine", "Mille", "Torben", "Troels", "Søren"]
management = ["Tine", "Trunte", "Rane"]
employees = ["Niels", "Anna", "Tine", "Ole", "Trunte", "Bent", "Rane", "Allan", "Stine", "Claus", "James", "Lars"]


'''
1.who in the board of directors is not an employee?
'''
'''
2.who in the board of directors is also an employee?
'''


for i in directors:
    if employees.__contains__(i):
        print("is a employee: " + i)
    else:
        print("Is not a employee: " + i)

print()

'''
how many of the management is also member of the board?
'''


x = 0
for i in directors:
    if management.__contains__(i):
        x = x + 1

print("There are " + str(x) + " who is a member of the board")
print()


'''
All members of the managent also an employee
'''


if(set(management).issubset(set(employees))):
    print("All members of the management is an employee")
else:
    print("All Members of the management is not in board")

print()

'''
All members of the management also in the board?
'''
if(set(management).issubset(set(directors))):
    print("true")
else:
    print("All Members of the management is not in board")

print()
'''
Who is an employee, member of the management, and a member of the board?
'''
for i in employees:
    if directors.__contains__(i) and management.__contains__(i):
        print(i + " is member of management and board")
print()
'''
Who of the employee is neither a memeber or the board or management?
'''
for i in employees:
    if not directors.__contains__(i) and not management.__contains__(i):
        print(i + " is not a member of the board and management")

print()


