
# T.C - O(N*N)
# S.C - O(1)
def  maxSubArray(arr):
    n = len(arr)
    maxi = float('-inf')
    for i in range(n):
        sum = 0

        for j in range(i,n):
            sum += arr[j]
            maxi = max(maxi,sum)

    print(maxi)


# Kadane's Algorithm
# T.C - O(N)
# S.C - O(1)
def maxSubArray_opt(arr):
    n = len(arr)
    maxi = float('-inf')
    sum = 0
    for i in range(n):
        sum+=arr[i] 
        maxi = max(maxi, sum)
        if sum < 0:
            sum =0

    print(maxi)
        
arr = [ -2, 1, -3, 4, -1, 2, 1, -5, 4 ]

maxSubArray(arr)
maxSubArray_opt(arr)