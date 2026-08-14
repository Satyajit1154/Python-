'''
Attributes-
    Attributes are properties of Class.

There are 2 types of Attributes
    1.Class Attributes-
    2.Instance Attributes-
'''
class Student:
    college_name="KIT College of Engineering" #This is class variable
    PI=3.14 #This is also class attribute
    def __init__(self,name,gpa):
        self.name=name #This are instance attribute.
        self.gpa=gpa 
        self.PI=3.1

stu1=Student("Satyajit",8.4)
#this are instance attribute and can be instanctaited with obj name only.
print(stu1.name)
print(stu1.gpa)

#Class attribute can be called by both object and class name
print(stu1.college_name)
print(Student.college_name)

print(Student.PI)#Here 3.14 class value is printed
print(stu1.PI)#Here 3.1 Instance value is printed
