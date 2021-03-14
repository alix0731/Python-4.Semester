num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num2 - num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Type the rigth operator...")

############################################

# når man bruger split sp deler den string op i arrayet og fjener den tegn som man har sagt at den skal deles sig op
# der hvor der er mellemrum
num = input("indtast et regnestykke: ").split(" ")
# hvis istedet brugt list1 = list(), så bliver hele alt sat ind i arrayet med mellemrum


print(num)

if num[1] == "+":
    print(float(num[0]) + float(num[2]))
elif num[1] == "-":
    print(float(num[0]) - float(num[2]))
elif num[1] == "*":
    print(float(num[0]) * float(num[2]))
else:
    print("Wrong operator...")

