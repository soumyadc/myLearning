#!/usr/bin/python

# All arg passed in a function are by default passed by reference.
# that means if the value of arg is changed inside a function it gets
# reflected in the caller also.

def changeme(myList):
    # myList is already passed by reference. lets change it here
    print("Original Value of myList (inside function): ", myList)
    myList[2]=500000
    print("Changed Value of myList (inside function): ", myList)
    return


list=[1,2,3,4,5,6,7,8,9,10]
print("Value of myList (before function call): ", list)
changeme(list)
print("Value of myList (after function call): ", list)
