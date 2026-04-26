def rotate_right(arr,n):
    temp = [0]*n

    for i in range(0,n-1):
        temp[i+1] = arr[i]
    
    temp[0] = arr[n-1]

    for num in temp:
        print(num,end=" ")
    print()


def rotate_right_opt(arr, n):
    temp = arr[n-1]

    for i in range(n-2, -1, -1):
        arr[i+1] = arr[i]

    arr[0] = temp

    for num in arr:
        print(num,end=" ")
    print()


n = 5
arr = [1, 2, 3, 4, 5]

rotate_right(arr, n)        # [5,1,2,3,4]
rotate_right_opt(arr, n) 
rotate_right(arr, n)