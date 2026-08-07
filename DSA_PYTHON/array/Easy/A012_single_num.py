# T.C - O(N*N)
# S.C - O(1)
def getSingleElement_linear(arr):
    n = len(arr)

    for i in range(n):
        count = 0
        num = arr[i]
        for j in range(n):
            if num == arr[j]:
                count+=1
        if count == 1:
            print(num)


# T.C - O(N)
# S.C - O(N)
def getSingleElement_map(arr):
    freq ={}
    for num in arr:
        freq[num] = freq.get(num,0)+1

    for x,y in freq.items():
        if y==1:
            print(x)

# T.C - O(N)
# S.C - O(1)
def getSingleElement(arr):
    xor = 0
    for num in arr:
        xor= xor ^ num
    
    print(xor)


arr = [4, 1, 2, 1, 2]
getSingleElement(arr)
getSingleElement_map(arr)
getSingleElement_linear(arr)