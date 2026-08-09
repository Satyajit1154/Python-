'''
Tuples- immutable sequence of values 
        Tuples can also store different data type values 
        like lists.
'''
tup=(1,2,3,4,5,"abc",3.14)

print(tup)
'''We cannot change values of tuples'''

for val in tup:
    print(val)

tup1=(1,2,3,4,5,6)
sum=0
for val in tup1:
    sum +=val
print(f"sum of values is {sum}")

'''Tuple methods'''
tup3=(1,2,2,3,4,5,6)

print(tup3.index(2)) #this method gives first index of 2 in tuple

print(tup3.count(2)) #this method returns count of 2