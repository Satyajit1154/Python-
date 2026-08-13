'''
Constructor:
    constructor is a method which gets called everytime 
    when we create a object

    __init__Method is special method which is called everytime  object is called 
'''

class Student:
    def __init__(self,name):
        print("constructor was called..")
        

stu1=Student("Satyajit")

class Studnet:
    def __init__(self,name):
        self.name=name
stu1=Studnet("satyajit")
print(stu1.name)
