# T.C - O(N*N)
# S.C - O(1)
def longestSubarray_bruteforce(arr, k):
    n = len(arr)
    maxlen = 0
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += arr[j]

            if sum == k:
                maxlen = max(maxlen,j-i+1)
    
    print(maxlen)
    return maxlen
 
# T.C - O(N)
# S.C - O(1)
def longestSubarray_opt(arr, k):
    left = 0
    sum =0
    maxlen =0

    for right in range(len(arr)):
        sum+= arr[right]

        while left <= right and sum >k:
            sum -= arr[left]
            left +=1
        
        if sum == k:
            maxlen = max(maxlen, right - left +1)
    
    print(maxlen)
    return maxlen


arr = [1, 2, 2, 1, 5]
k = 4

longestSubarray_bruteforce(arr,k)
longestSubarray_opt(arr,k)
