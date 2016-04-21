#!/usr/bin/python

import os
import io

    
fo = open("./tmp1.txt", "r+")
# Method 1: readline()
print "Method 1: readline()"
str = "null"
while str:
    str = fo.readline()
    print (str)

# Method 2: for line in file
print "Method 2: for line in file:"
fo.seek(0,0)
for line in fo:
    print(line)
    

# Method 3: reladlines() to a list
print "Method 3: reladlines() to a list"
fo.seek(0,0)
buf =fo.readlines()
print (buf)
print ("Number of lines: ", len(buf))

#for x in buf:
#    print(x)


fo.close()

#Modify line number 4
print "Modify line number 4"
buf[3] = "I have changed the line number 4\n" 

# Write Lines in a tmp2.txt file
print "Write Lines in a tmp2.txt file"
fo=open("./tmp2.txt", "w+")
fo.seek(0,0)
fo.writelines(buf)
fo.seek(0,0)
buf =fo.readlines()
print (buf)
fo.close()
