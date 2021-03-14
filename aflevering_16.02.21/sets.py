set1 = {'a', 'e', 'i', 'o', 'u', 'y'}

set2 = {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}


#Union
print(set1.union(set2))


print()

#Symmetric Difference, viser hvilken ord der er forskellige fra de to sets
print(set1.symmetric_difference(set2))

print()

#Difference 
print(set1.difference(set2)) # no difference, 
print(set2.difference(set1)) 

print()

#Disjoint, det er når 2 sets har ingen elementer tilfælles
print(set1.isdisjoint(set2))