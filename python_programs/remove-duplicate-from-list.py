# Ref: https://favtutor.com/blogs/remove-duplicates-from-list-python

# ==================================================================
# 1) Using list comprehensive + enumerate()

sam_list = [11, 15, 13, 16, 13, 15, 16, 11] 
print ("The list is: " + str(sam_list)) 

# to remove duplicated from list 
result = [i for n, i in enumerate(sam_list) if i not in sam_list[:n]] 

# printing list after removal 
print ("The list after removing duplicates: " + str(result)) 

# ==================================================================
# 2) Using collections.OrderedDict.fromkeys()

# removing duplicated from list using collections.OrderedDict.fromkeys() 
from collections import OrderedDict 

# initializing list 
sam_list = [11, 15, 13, 16, 13, 15, 16, 11] 
print ("The list is: " + str(sam_list)) 

# to remove duplicated from list 
result = list(OrderedDict.fromkeys(sam_list)) 

# printing list after removal 
print ("The list after removing duplicates: " + str(result)) 