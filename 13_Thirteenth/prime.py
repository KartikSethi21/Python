numb = int(input("Enter a number "))

is_prime = True

if numb>1:
    for i in range(2,numb):
        if numb% i ==0:
            is_prime=False
            break
print(is_prime)