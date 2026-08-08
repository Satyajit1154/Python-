'''
Functions- blocks of statement that perform a specific task
'''
#functions defination-
def hello():
    print("hello")
#functions call
hello()


def sum(a,b):
    s=a+b
    return s
ans=sum(3,4)
print(ans)

#Functions with parameters 
def calc_avg(a,b,c):
    sum=a+b+c
    return sum/3
ans=calc_avg(10,20,30)
print(ans)

#Functions with default values 
def calc_avg(a=10,b=20,c=30):
    sum=a+b+c
    return sum/3
ans=calc_avg()
print(ans)

'''There are 2 types of Function
    1. Built in-
               print()
               input()
               type()
               range()
    2. user defined-functions that we define and call
                sum()
                calc_avg().....
                


'''