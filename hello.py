#!/usr/bin/env python

import sys

def gotname(name): #when called prints the Hello and the name from the argument list.
    print("Hello %s!" % (name))

def world(): #when called, prints Hello World!
    print("Hello World!")

i=0
for i in range(0,len(sys.argv)-1):
    gotname(sys.argv[i+1]) #calls the gotname function. (i+1) is needed becasue the first argument would be hello.py in the list
    i+=1
if i==0: #if no arguments was given in the command line calls the world() function
    world()
