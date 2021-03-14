 
# Initialization of dictionary 
dict = {"a": "Alpha", "b" : "Beta", "g": "Gamma"}


  
# Converting into list of tuple 
#list = [(k, v) for k, v in dict.items()] 

list = [(key, value) for key, value in dict.items()]
  
# Printing list of tuple 
print(list) 