

friends = []

while len(friends) < 3:
    friends.append(input("Enter friend name: "))


print(friends)  

print(friends[::-1])


def change(list, index, new):
    list[index] = new
    return list

index  = input("Enter index to change: ")
indput = input("Enter new input at index:")

print(change(friends, int(index), indput))


list1 = [1,3,5,6]

print(list1[1:])
 












