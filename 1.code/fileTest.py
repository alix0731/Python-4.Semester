
### create a file 
'''
myFile = open("myFile.txt", "w")
myFile.close()
'''


## write to a file
'''
myFile = open("myFile.txt", "a")
myFile.write("Hvad laver du?")
myFile.close()
'''


## read a file

myFile = open("myFile.txt", "r")
print(myFile.read())
myFile.close()

