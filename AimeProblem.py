#This is a programatic solution on trying to solve 2021 AIME II Question 15.
from math import floor, sqrt

n = 1

def f(n): 
    #checking for a perfect square
    x = floor(sqrt(n))
    if x == sqrt(n):
        return x
    else:
        #recurse into the function 
        return 1 + f(n+1)

def g(n): 
    #checking for a perfect square
    x = floor(sqrt(n))
    if x == sqrt(n):
        return x
    else:
        #recurse into the function 
        return 2 + g(n+2)

#print the first occurrence of n for which f(n)/g(n) is 4/7
while f(n)/g(n) != 4/7:
    n=n+1

print(n) 


