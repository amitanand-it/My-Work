import sys

my_list = []

for i in range(100000000): my_list.append(i)
print(sys.getsizeof(my_list))  # Memory usage for the list

my_tuple = tuple(my_list)
print(sys.getsizeof(my_tuple))  # Memory usage for the tuple



#Time checking 
import time

start = time.time()
for x in my_list: pass
duration = time.time() - start
print("Duration for List: ", duration )


start = time.time()
for x in my_tuple: pass
duration = time.time() - start
print("Duration for Tuple: ", duration )

