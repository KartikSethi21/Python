# WAP that take n number of inputs and retur their sum
def sum_all(*args):
    print(*args)
    print(args)
    for i in args:
        print(i*2)
    return sum(args,start=2)

# sum(args) → 1 + 2 + 3 = 6
# start=2 → adds 2 to the sum
print("Sum is",sum_all(1,2,3))

# print(sum_all(1,2,3,5,6))
# print(sum_all(1,2,3,98,12))
# print(sum_all(1,2,3,654))