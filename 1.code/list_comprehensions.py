


a = [chr(i) for i in range(65, 91) if i != 70]
print(a)

b = [chr(i) for i in range(65, 91) if i%2 == 0]

print(b)



#  2.Clothes List Comprehension

colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']

cloth = [(i, j) for i in colors for j in sizes]
print(cloth)



num = [i*2 for i in range(10)]

print(num)



z = [chr(i) for i in range(65, 91)]

print("this is z " + str(z))


