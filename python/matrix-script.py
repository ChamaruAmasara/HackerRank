#https://www.hackerrank.com/challenges/matrix-script/problem

#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

string=""
x=len(matrix[0])
for x in range(len(matrix[0])):
    for matrix_item in matrix:
        string+=matrix_item[x]
i=0
newstring=""
while i<len(string):
    while i<len(string) and string[i].isalnum():
        newstring+=string[i]
        i+=1
    else:
        newstring+=" "
    i+=1
    
        

newstring=newstring.strip()
stringList=newstring.split()
while newstring:
    i=0
    start=""
    while string[i]!=newstring[0]:
        
        start+=string[i]
        i+=1
        

    i=len(string)-1
    end=""
    while string[i]!=newstring[-1]:
        end=string[i]+end
        i-=1
    print(start+" ".join(stringList)+end)
    break
while not(newstring):
    print(string)
    break