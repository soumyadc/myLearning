#!/usr/bin/python

# A Generator:
# helps to generate a iterator object by adding 1-by-1 elements in iterator.
# it uses yield
# yield __must__ be used inside a function

#A generator is a function that produces or yields a sequence of values using yield method.

def func():
    count = 0
    while count < 10:
        yield count
        count += 1
    return     


it=func() # it is out iterator object here

while True:
    try:
        print (next(it))
    except:
        break
    
print("GoodBye")


