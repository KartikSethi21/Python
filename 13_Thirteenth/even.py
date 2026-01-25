#count sum of even number upto n

n = int(input("Enter value of n "))

count=0
for i in range(1,n+1):
    if i%2 ==0:
        count+=i
        print(count)

print(f"Sum of even number upto n {count}")