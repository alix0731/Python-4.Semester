## 2D Lists

lists =[
    [1,2,3],
    ["Ali", "Raza", "Akhtar"],
    [4,5,6]
]


print(lists[1][2])



### Nested loops

for row in lists:
    for col in row:
        print(col)


#for i in range(2):
 #   print("this is first loop")
  #  for x in range(2):
   #     print("this is second loop")