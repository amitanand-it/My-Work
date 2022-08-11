"""
# First Approach: Using a  Freezer class
"""
class Freezer:

    '''Freeze any class, such that instantiated objects become immutable.  '''
    _frozen = False

    def __init__(self):
        self._frozen = True

    def __delattr__(self, *args, **kwargs):
        if self._frozen:
            raise AttributeError('This object is frozen!')
        object.__delattr__(self, *args, **kwargs)

    def __setattr__(self, *args, **kwargs):
        if self._frozen:
            raise AttributeError('This object is frozen!')
        object.__setattr__(self, *args, **kwargs)


class ImmutableClass(Freezer):

    def __init__(self, name, age) -> None:
            self.name = name
            self.age = age

            super().__init__()

# obj1 = ImmutableClass('Amit', 40)
# obj1.year = 'A'
# print(obj1.name, obj1.age, obj1.__dict__)

"""
# Approach 2: Freezer class with slots
"""

class Freezer:

    __slots__ = [] 
    '''Freeze any class, such that instantiated objects become immutable.  '''
    _frozen = False

    def __init__(self):

        # generate __slots__ list dynamically
        for attr_name in dir(self):
            self.__slots__.append(attr_name)

        self._frozen = True


    def __delattr__(self, *args, **kwargs):
        if self._frozen:
            raise AttributeError('This object is frozen!')
        object.__delattr__(self, *args, **kwargs)

    def __setattr__(self, *args, **kwargs):
        if self._frozen:
            raise AttributeError('This object is frozen!')
        object.__setattr__(self, *args, **kwargs)


class ImmutableClass(Freezer):

    def __init__(self, name, age) -> None:
            self.name = name
            self.age = age

            super().__init__()


obj1 = ImmutableClass('Amit', 40)
# obj1.year = 'A'
print(obj1.name, obj1.age, obj1.__dict__)