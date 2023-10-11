# SINGLETON USING META CLASS

class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            #cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonClass(metaclass=SingletonMeta):
    def __init__(self):
        self.value = None


obj1 = SingletonClass()
obj1.value = "Object 1"

obj2 = SingletonClass()
obj2.value = "Object 2"

obj3 = SingletonClass()
obj3.value = "Object 3"
obj3.name = "Amit"

print("obj1 == obj2: ", obj1 == obj2)
print(f"obj1: {obj1}\nobj2: {obj2}\nobj3: {obj3}")
print(f"data1: {obj1.__dict__}")
print(f"data2: {obj2.__dict__}")

