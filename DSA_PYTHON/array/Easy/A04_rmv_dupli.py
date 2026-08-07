def rmv_dupli(arr):
    arr = list(set(arr))
    print(arr)
    # If order doesnot matter

# T.C - O(N)
# S.C - O(N)
def rmv_dupli_bf(arr):
    seen =set()

    ind = 0
    for num in arr:
        if num not in seen:
            seen.add(num)
            arr[ind] = num
            ind+=1
    
    return ind

# T.C - O(N)
# S.C - O(1)
def rmv_dupli_opt(arr):
    i = 0
    for j in range(i+1,len(arr)):
        if arr[i] != arr[j]:
            i+=1
            arr[i] = arr[j]
    return i+1



arr = [1,1,1,2,2,3,4,5]
rmv_dupli(arr)
arr = [1,1,1,2,2,3,4,5]
i = rmv_dupli_bf(arr)
print(arr[:i])
arr = [1,1,1,2,2,3,4,5]
i = rmv_dupli_opt(arr)
print(arr[:i])