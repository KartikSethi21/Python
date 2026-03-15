numb = int(input("Enter a number "))
x=numb
fact = 1
while x>0:
    fact *= x
    x-=1


print(f"Fatorial of {numb} is {fact}")