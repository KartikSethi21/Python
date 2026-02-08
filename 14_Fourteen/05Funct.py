# Recursive Functions

def factorial(n):
    if n==1: return 1
    return n*factorial(n-1)
print(factorial(5))

def sum(n):
    if n==1: return 1
    return n+sum(n-1)
def fibon(n):
    if n==0 or n==1 : return n
    
print(sum(10))