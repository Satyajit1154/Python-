'''
List-mutable sequence of Values
datatype can be any type in sing list 
'''

marks=[99,89,100,65,92]
print(marks)
print(len(marks))

marks[0]=70
print(marks)

data=["abc",70,20,"xyz",True]
print(data)

'''List can also be sliced'''
print(data[0:3])



'''There are various methods in lists'''
data.append(20)
print(data)

#add at specific index here 2  is index and 10 is data to be added 
data.insert(2,10)
print(data)

nums=[90,10,70,80,30]
nums.sort()
print(nums)

nums.reverse()
print(nums)

for val in nums:
    print(val)