"""
# Ref: https://towardsdatascience.com/python-tuples-when-to-use-them-over-lists-75e443f9dcd7#:~:text=key%20takeaways%20are%3B-,The%20key%20difference%20between%20the%20tuples%20and%20lists%20is%20that,memory%20efficient%20than%20the%20lists.
# 
#

They are both used to store collection of data
They are both heterogeneous data types means that you can store any kind of data type
They are both ordered means the order in which you put the items are kept.
They are both sequential data types so you can iterate over the items contained.
Items of both types can be accessed by an integer index operator, provided in square brackets, [index]

The key difference between the tuples and lists is that while the tuples are immutable objects the lists are mutable. This means that tuples cannot be changed while the lists can be modified.


As lists are mutable, Python needs to allocate an extra memory block in case there is a need to extend the size of the list object after it is created. In contrary, as tuples are immutable and fixed size, Python allocates just the minimum memory block required for the data.

As a result, tuples are more memory efficient than the lists.
"""

import sys
a_list = list()
a_tuple = tuple()
a_list = [1,2,3,4,5]
a_tuple = (1,2,3,4,5)
print(sys.getsizeof(a_list))
print(sys.getsizeof(a_tuple))
# Output:
# 104 (bytes for the list object
# 88 (bytes for the tuple object)


"""

As you can see from the output of the above code snippet, the memory required for the identical list and tuple objects is different.

When it comes to the time efficiency, again tuples have a slight advantage over the lists especially when lookup to a value is considered.


"""


import sys, platform
import time
print(platform.python_version())
start_time = time.time()
b_list = list(range(10000000))
end_time = time.time()
print("Instantiation time for LIST:", end_time - start_time)
start_time = time.time()
b_tuple = tuple(range(10000000))
end_time = time.time()
print("Instantiation time for TUPLE:", end_time - start_time)
start_time = time.time()
for item in b_list:
  aa = b_list[20000]
end_time = time.time()
print("Lookup time for LIST: ", end_time - start_time)
start_time = time.time()
for item in b_tuple:
  aa = b_tuple[20000]
end_time = time.time()
print("Lookup time for TUPLE: ", end_time - start_time)
# Output:
# 3.6.9
# Instantiation time for LIST: 0.4149961471557617 
# Instantiation time for TUPLE: 0.4139530658721924 
# Lookup time for LIST:  0.8162095546722412 
# Lookup time for TUPLE:  0.7768714427947998
