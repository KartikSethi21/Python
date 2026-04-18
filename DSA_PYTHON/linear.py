def linear(arr, n, k):
    if n==0: return -1

    for i in range(n):
        if arr[i] == k:
            return i
        
    return -1


arr = [1,5,6,8,44,12,44,65]
n = len(arr)
print(linear(arr,n,5))