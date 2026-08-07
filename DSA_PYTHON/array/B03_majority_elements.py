# T.C - O(N**2)
# S.C - O(1)
def majority_element_bf(arr):
    n = len(arr)
    for i in range(n):
        cnt = 0 
        ele = arr[i]
        for j in range(n):
            if arr[j] == ele:
                cnt+=1
        if cnt > (n//2):
            return ele
        
    return -1

# T.C - O(N)
# S.C - O(N)
def majority_element_best(arr):
    freq = {}
    n = len(arr)

    for ele in arr:
        freq[ele] = freq.get(ele,0)+1

    for x, y in freq.items():
        if y > (n//2):
            return x
        
    return -1

# T.C - O(1)
# S.C - O(1)
# Moore’s Voting Algorithm` `
def majority_element_opt(arr):
    cnt = 0
    ele = arr[0]
    n = len(arr)
    for num in arr:
        if cnt==0:
            cnt = 1
            ele = num
        elif num != ele:
            cnt-=1
        else:
            cnt+=1

    
    cnt1 = arr.count(ele) 

    if cnt1 > (n//2):
        return ele
    
    return -1

arr = [2, 2, 1, 1, 1, 2, 2]
print(majority_element_bf(arr))
print(majority_element_best(arr))
print(majority_element_opt(arr))