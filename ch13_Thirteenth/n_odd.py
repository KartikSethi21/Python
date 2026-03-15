n = int(input("Enter a number "))
# T.C - O(n), S.C - O(1)
start =1
total =0
# Print n odd numbers
for _ in range(n):
    print(start)
    total+=start
    start+=2

#sum of n odd numbers
# start =1
# total =0
# for i in range(1,n+1):
#     total+=start
#     start+=2

print(f"Sum of n odd numbers is {total}")

# Version 2
# T.C - O(n), S.C - O(1)

# total = 0
# for odd in range(1, 2*n, 2):
#     print(odd)
#     total += odd

# Version 3
# T.C - O(1) ,  S.C - O(1)

total = n*n
print(f"Total sum of {n} odd numbers is {total}")
# -----------Even
total = n*(n+1)
print(f"Total sum of {n} even numbers is {total}")
# ------------all numbers natiral
total = n*(n+1) // 2
print(f"Sum of first {n} numbers is {total}")