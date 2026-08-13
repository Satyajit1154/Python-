class Student:
    def __init__(self,name,cgpa):
        self.name=name
        self.cgpa=cgpa
    def get_cgpa(self):
        return self.cgpa

stu1=Student("Satyajit",9.0)
print(stu1.get_cgpa())

'''There are 2 types of Constructors
    1.default
    2.Parameterized 

'''
