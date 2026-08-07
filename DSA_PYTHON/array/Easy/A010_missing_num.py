

# T.C O(n*n)
# S.C O(1)
def missing_linear(arr):
    n = len(arr)

    for i in range(1,n+2):
        found = False

        for j in range(n):
            if arr[j] == i:
                found = True
                break
        if not found:
            return i
    

    return -1


# T.C O(n)
# S.C O(n)
def missing_map(arr):
    n = len(arr)
    freq = [0] * (n+2)

    for i in range(n):
        freq[arr[i]]+=1

    # print(freq)  #[0, 1, 1, 1, 1, 1, 0, 1, 1] => array

    for i in range(1,n+2):
        if freq[i] == 0:
            return i
    
    return -1

# T.C O(n)
# S.C O(1)
def missing_sum(arr): 
    n = len(arr)
    total = sum(arr)
    expected = 0
    # for i in range(1,n+2):
    #     expected+=i
    n = n+1
    expected = (n * (n+1) ) // 2
    missing = expected - total

    return missing

# T.C O(n)
# S.C O(1)
def missing_xor(arr):
    xor1, xor2  = 0, 0
    n = len(arr)
    for i in range(n):
        xor1 = xor1 ^ arr[i]
    
    for i in range(1,n+2):
        xor2 = xor2 ^ i
    
    return xor2 ^ xor1

arr = [8, 2, 4, 5, 3, 7, 1]
res = missing_linear(arr)
print(res)
res = missing_map(arr)
print(res)
res = missing_sum(arr)
print(res)

res = missing_xor(arr)
print(res)

