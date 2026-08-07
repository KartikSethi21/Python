# T.C - O(n)
# S.C - O(n)

def rotate_k_right(arr, n, k):
    temp = [0]*n
    k = k % n
    for i in range(n):
        temp[ (i+k) % n] = arr[i]

    for num in temp:
        print(num,end=" ") 
    print()

# T.C - O(n)
# S.C - O(n)
def rotate_k_left(arr, n, k):
    temp = [0]*n
    k = k % n
    for i in range(n):
        temp[ (i-k) % n] = arr[i]

    for num in temp:
        print(num, end=" ")
    
    print()

arr = [1,2,3,4,33,21,54]
n = len(arr)
rotate_k_right(arr,n,3)

rotate_k_left(arr,n,3)

print(arr[:])


# T.C - O(N)
# S.C - O(k) 

def rotateRight(self, arr, k):
    n = len(arr)
    if n == 0:
        return
    k %= n
    # Store last k elements
    temp = arr[-k:]
    # Shift the remaining elements
    for i in range(n - k - 1, -1, -1):
        arr[i + k] = arr[i]
    # Copy stored elements to the front
    for i in range(k):
        arr[i] = temp[i]
# Rotate the array to the left by k positions
def rotateLeft(self, arr, k):
    n = len(arr)
    if n == 0:
        return
    k %= n
    # Store first k elements
    temp = arr[:k]
    # Shift remaining elements
    for i in range(k, n):
        arr[i - k] = arr[i]
    # Copy stored elements to the end
    for i in range(k):
        arr[n - k + i] = temp[i]

















def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end] , arr[start]
        start+=1
        end-=1
# reverse(arr,0,n-1)
# print(arr[:])

# T.C - O(N)
# S.C - O(1)
def rotate_k_opt(arr, k, dir):
    n= len(arr)
    if n==0 or k==0:
        return arr
    k = k % n

    if dir == "right":
        reverse(arr,0,n-1) # reverse full array
        reverse(arr,0,k-1) # reverse first k elements
        reverse(arr,k,n-1) # reverse remaining elements
    
    elif dir == "left":
        reverse(arr, 0, k-1) #reverse first k elements
        reverse(arr,k, n-1) #reverse remaining elements   
        reverse(arr,0,n-1) #reverse full array

rotate_k_opt(arr,2,"right")
print(arr[:])
rotate_k_opt(arr,2,"left")
print(arr[:])