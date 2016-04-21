#!/usr/bin/python

# iterator supports 2 methods: iter(var_list) and next(var_iter)

list = [1,2,3,4,5] # This defines the list

it = iter(list) # this builds an iterator object

for x in it:
    print(x)
print ("GoodBye")
