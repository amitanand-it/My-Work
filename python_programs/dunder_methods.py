
class Employee:

    def __new__(cls):
        print ("__new__ magic method is called")
        inst = super().__new__(cls, *args, **kwargs)
        return inst

    def __init__(self, name):
        print ("__init__ magic method is called")
        self.name = name
        print("Name set ", self.name)

#e = Employee(name="Amit Anand")
e = Employee(name="Amit")
