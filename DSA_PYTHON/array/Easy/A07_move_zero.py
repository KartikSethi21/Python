# T.C - O(N)
# T.C - O(N)

def move_zero_bf(arr):
    n = len(arr)

    temp = [0]*n
    index = 0
    for i in range(n):
        if arr[i] != 0:
            temp[index] = arr[i]
            index+=1
    
    arr[:] = temp[:]
    print(arr[:])


def move_zero_opt(arr):
    nonzero=0
    n = len(arr)
    for i in range(n):
        if arr[i] !=0:
            arr[nonzero] , arr[i] = arr[i], arr[nonzero]
            nonzero+=1

arr = [0, 1, 0, 3, 12]
move_zero_bf(arr)
arr = [0, 1, 0, 0, 4, 112, 0]
move_zero_opt(arr)
print(arr)