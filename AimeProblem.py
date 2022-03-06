from math import floor, sqrt

n = 1
answerList = []

def f(n):
    x = floor(sqrt(n))
    if x == sqrt(n):
        return x
    else:
        return 1 + f(n+1)

def g(n):
    x = floor(sqrt(n))
    if x == sqrt(n):
        return x
    else:
        return 2 + g(n+2)


for n in range(1,10000):
    if f(n)/g(n) == 4/7:
        answerList.append(n)

print(answerList)


