#Create an empty set

s = set()

#Add elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)#this is not as a list, same element will not be printed again

s.remove(2)
print (s)

print(f"The set has {len(s)} elements.")
