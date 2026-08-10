'''
Sets: Collection of Unique Elements
        Each element is immutable  
'''
s={1,2,3,4,4} #4 will be stored only once 
print(s)

#empty set 
empty_set=set()
print(type(s))

s.add(5)
print(s)
s.pop()
print(s)

s2={1,2}
print()

print(s.union(s2))
print(s.intersection(s2))

