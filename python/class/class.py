#!/usr/bin/python

# define call employee
class Employee:
    emp_count=0 #this is global. applicable for all objs

#counstructor
    def __init__(self, name, salary):
        self.name = name # define the object specific variables here
        self.salary = salary
        return

#destructor
    def __del__(self):
        class_name= self.__class__.__name__
        print(class_name, " destroyed")
        return

#self.emp_count cannot be used here. instead
#Employee.emp_count should be updated so that it can be used as global
        Employee.emp_count +=1
        print("Employ: %s created" % self.name)
        return
    
    def displayCount(self):
        print ("Total Employee Count: %d" % Employee.emp_count)
        return

    def displayEmp(self):
        print ("Name: ", self.name, "Salary: ", self.salary) 
        return

       
#Define a new object for Employee class
# SYNTAX:  obj = <class>(<__init__ args>)       
emp1 = Employee(name="aaaa", salary="10000")
emp2 = Employee(name="bbbb", salary="20000")
emp3 = Employee(name="cccc", salary="30000")
emp4 = Employee(name="dddd", salary="40000")
emp5 = Employee(name="eeee", salary="50000")

print ("Total Employee Count: %d" % Employee.emp_count)


emp1.displayEmp()
emp2.displayEmp()
emp3.displayEmp()
emp4.displayEmp()
emp5.displayEmp()



# hasattr(emp1, 'salary')    # Returns true if 'salary' attribute exists
# getattr(emp1, 'salary')    # Returns value of 'salary' attribute
# setattr(emp1, 'salary', 7000) # Set attribute 'age' at 8
# delattr(emp1, 'salary')    # Delete attribute 'age'

print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__ )

#Now destroy the objects
del emp1
