print("START")
arr = map(int,input().split())
# print(arr)
for num in arr:
    print(num,end = " ")

# arr = int(input())
# print(arr)


print("\nSTART")
arr = map(int,list(input()))
# print(arr)
for num in arr:
    print(num,end = " ")


if __name__ == '__main__':
    print("\nSTART 1 ")
    arr = map(int,input().split())
    first = float('-inf')
    sec = float('-inf')

    for num in arr:
        if num > first :
            sec = first
            first = num
        if num >sec and num != first:
            sec = num
    print(sec)


a = [["k",21],["k",14],["a",90]]
a = sorted(a)
print(a)


for x,y in a:
    print(x)
    print(y)

sc = [ y for x , y in a]
print(sc)

for num in a:
    print(num)