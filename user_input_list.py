# user input list extend program
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 20:03:18 2022

@author: Dhaval
"""
print("your list is: ")
num=[1,2,3]
#print(type(num))
print(num)
n=int(input("\n Enter list size you want to create: "))
i=1
while i<=n:
    jp=int(input("Enter List elements: "))
    num.extend([jp])
    i=i+1
i=1
while i<=n:
    i=i+1
print(num)

reset=input("If you wont to Reset this list Enter 'Yes' or 'No' ")
if reset=='yes':
    del num
    print("Reset is done")
else:
    print("End Program")
    print(num)
#elif reset=

 
 
