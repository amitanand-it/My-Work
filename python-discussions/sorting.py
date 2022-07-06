# REFERENCE: https://docs.python.org/3.8/howto/sorting.html

"""
can we sort a dictionary using sort() method   ? 
list.sort() method is only defined for lists. In contrast, the sorted() function accepts any iterable
"""

d = dict(d=4, e=5, a=1, b=2, c=3)
# Below line will give error as sort is only applicable on lists
# d.sort()

print(sorted(d.items()))
# OUT: [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]

print(sorted(d))
# OUT: ['a', 'b', 'c', 'd', 'e']

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
QUESTION : Do case-insensitive string comparison:
key=str.lower
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
str_list = "This is a test string from Andrew".split()
sorted(str_list, key=str.lower)
['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
SORTING ON COMPLEX OBJECTS
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# 1)
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
# sort by age
sorted(student_tuples, key=lambda student: student[2])   
# OUT: [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]


# 2)
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]

sorted(student_objects, key=lambda student: student.age)



"""""""""""""""""""""""""""""""""""""""""""""""""""
SORTING USING OPERATOR MODULE
"""""""""""""""""""""""""""""""""""""""""""""""""""
from operator import itemgetter, attrgetter
sorted(student_tuples, key=itemgetter(2))
sorted(student_objects, key=attrgetter('age'))

# The operator module functions allow multiple levels of sorting.
# For example, to sort by grade then by age:
sorted(student_tuples, key=itemgetter(1,2))
# [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
sorted(student_objects, key=attrgetter('grade', 'age'))
# [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

"""""""""""""""""""""""""""""""""""""""""""""""""""
Ascending and Descending
"""""""""""""""""""""""""""""""""""""""""""""""""""
sorted(student_tuples, key=itemgetter(2), reverse=True)
sorted(student_objects, key=attrgetter('grade', 'age'), reverse=True)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Question: Is sort method stable ? 
when multiple records have the same key, their original 
order is preserved ? YES 
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
sorted(data, key=itemgetter(0))
# [('blue', 1), ('blue', 2), ('red', 1), ('red', 2)]


""""""""""""""""""""""""""""""""""""""""""""""""""""
ASCENDING ON AGE FIRST, THEN DESCENDING ON GRADE
"""""""""""""""""""""""""""""""""""""""""""""""""""
student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
    Student('new', 'A', 12),
]

s = sorted(student_objects, key=attrgetter('age'))     # sort on secondary key
print(sorted(s, key=attrgetter('grade'), reverse=True) )      # now sort on primary key, descending
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

print(sorted(student_objects, key=attrgetter('age', 'grade'), reverse=True))



"""""""""""""""""""""""""""""""""""""""""""""""""""
DECORATE-SORT-UNDECORATE  (Schwartzian transform)
"""""""""""""""""""""""""""""""""""""""""""""""""""
decorated = [(student.grade, i, student) for i, student in enumerate(student_objects)]
decorated.sort()
[student for grade, i, student in decorated]  # undecorate


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
The sort routines are guaranteed to use __lt__() when making comparisons 
between two objects. So, it is easy to add a standard sort order to a class 
by defining an __lt__() method:
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Student.__lt__ = lambda self, other: self.age < other.age
sorted(student_objects)
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Key functions need not depend directly on the objects being sorted. A key 
function can also access external resources. For instance, if the student 
grades are stored in a dictionary, they can be used to sort a separate list 
of student names:
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
students = ['dave', 'john', 'jane']
newgrades = {'john': 'F', 'jane':'A', 'dave': 'C'}
sorted(students, key=newgrades.__getitem__)
# ['jane', 'dave', 'john']