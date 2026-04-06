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