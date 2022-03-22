from math import floor, sqrt

n = 1
answerList = []

def f(n): #Defining what f(n) is which is given in the problem.
    x = floor(sqrt(n))
    if x == sqrt(n):
        return x
    else:
        return 1 + f(n+1)

def g(n): #Defining what g(n) is which is given in the problem.
    x = floor(sqrt(n))
    if x == sqrt(n):
        return x
    else:
        return 2 + g(n+2)


for n in range(1,10000): #We run our n from 1 to 10000 because the answer is in integer value ranging from 1-10000.
    if f(n)/g(n) == 4/7:
        answerList.append(n)
        break #We have to use a break so that we print just the first value that satisfies this problem.


print(answerList) #Finally, we print the answer we have in our list.


