#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
n=int(input())
l=[]
for i in range(n):
    x=input()
    y=list(x)
    l.append(y)
for i in range(1,n-1):
    for j in range(1,n-1):
        if (l[i][j]>l[i-1][j])and(l[i][j]>l[i][j+1])and(l[i][j]>l[i+1][j])and(l[i][j]>l[i][j-1]):
            l[i][j]="X"
for element in l:
    for i in element:
        print(i,end="")
    print(end='\n')
    
    #this problem mainly is on initialising array
