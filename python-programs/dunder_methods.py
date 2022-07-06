from functools import total_ordering

@total_ordering
class Employee():

#   def __new__(cls):
#       print ("__new__ magic method is called")
#       inst = super().__new__(cls, *args, **kwargs)
#       return inst

    def __init__(self, name, age=0):
  #      print ("__init__ magic method is called")
        self.name = name
        self.age = age 
  #      print("Name set ", self.name)

    def __str__(self):
        return f"Name is {self.name}"

    def __repr__(self):
        return f"{__class__.__name__}(name={self.name!r}, age={self.age!r})"

    def __gt__(self, other):
        return self.age > other.age 

    def __eq__(self, other):
        return self.age == other.age 

    """
    def __gt__(self, other):
        return self.age > other.age 

    def __eq__(self, other):
        return self.age == other.age 

    def __lt__(self, other):
        return self.age < other.age 

    """

#e = Employee(name="Amit Anand")
amit = Employee(name="Amit", age=23)
vips = Employee(name="Vipin", age=23)
print(amit, amit.age)
print(vips, vips.age)
print("amit >  vips: ", amit > vips)
print("amit < vips: ", amit < vips)
print("amit == vips: ", amit == vips)
print("amit >=  vips: ", amit >= vips)
print("amit <= vips: ", amit <= vips)

