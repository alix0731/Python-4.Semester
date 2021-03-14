### readfile


file1 = open("employees.txt", "r")

## printer hele filen
##print(file1.read())

## printer enkelte liner
#print(file1.readline())
#print(file1.readline())


## putter liner i en list
list = file1.readlines()
print(list[1])

## lukker filen
file1.close()


