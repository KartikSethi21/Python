# Time = O(N)
# Space = O(N)

def longestSubarray_forall(arr, k):
    prefix_sum =0
    mp = {}
    max_len = 0

    for i in range(len(arr)):
        prefix_sum += arr[i]

        if prefix_sum == k:
            max_len = i+1
        if (prefix_sum - k) in mp:
            max_len = max(max_len, i - mp[prefix_sum - k])
        if prefix_sum not in mp:
            mp[prefix_sum] = i
    
    print(max_len)
    return max_len

arr = arr = [9, -3, 3, -1, 6, -5]
k = 5

longestSubarray_forall(arr,k)