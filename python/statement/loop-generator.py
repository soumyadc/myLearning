#!/usr/bin/python

# A Generator:
# helps to generate a iterator object by adding 1-by-1 elements in iterator.

#A generator is a function that produces or yields a sequence of values using yield method.

def fibonacci(n): #define the generator function
    a, b, counter = 0, 1, 0 # a=0, b=1, counter=0
    while True:
        if(counter > n):
            return
        yield a
        a=b
        b=a+b
        counter += 1


it=fibonacci(5) # it is out iterator object here

while True:
    try:
        print (next(it))
    except:
        break
    
print("GoodBye")


