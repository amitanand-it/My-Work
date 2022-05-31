class Employee():

    def __init__(self, name):
        self.name = name


class Student():

    def __init__(self, name):
        self.name = name

    def details(self):
        print (f" Name: {self.name}")

s = Student(name="Amit Anand")
# BOUND WAY OF CALLING DETAILS METHOD
s.details()
# UNBOUND WAY OF CALLING DETAILS METHOD
Student.details(s)

e = Employee(name="Sunil Anand")
# USING DETAIL METHOD OF STUDENT CLASS FOR EMPLOYEE OBJECT
Student.details(e)


