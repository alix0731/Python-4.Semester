def cube(num):
    return num*num*num

result = cube(3)

print(result)

if result is not 7 and 3 < 5:
    print("Rigtig")
else:
    print("Forkert")



is_male = False
is_tall = True
if is_male and is_tall:
    print("You are a high Male ")
elif is_male and not is_tall:
    print("You are a short male")
elif not is_male and is_tall:
    print("You are tall and not a male")
else:
    print("What are you then?")



def max_num(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        print(n1 , "is biggest")
    elif n2 >= n1 and n2 >= n3:
        print(n2 , "is biggest")
    else:
        print(n3 ,"is biggest")


print(max_num(34,54,65))

