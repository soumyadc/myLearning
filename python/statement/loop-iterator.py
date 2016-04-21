#!/usr/bin/python

# iterator supports 2 methods: iter(var_list) and next(var_iter)

list = [1,2,3,4,5] # This defines the list

it = iter(list) # this builds an iterator object

#prints next available element in iterator. every time next() is called next value is fetched from iter operator
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
