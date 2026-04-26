def rotate_left(arr, n):
    temp = [0]*n
    for i in range(1,n):
        temp[i-1] = arr[i]

    temp[n-1] = arr[0]

    for num in temp:
        print(num,end=" ")
    print()



def rotate_left_opt(arr,n):
    temp = arr[0]
    for i in range(1,n):
        arr[i-1] = arr[i]

    arr[-1] = temp

    for num in arr:
        print(num,end=" ")
    print()
n = 5  # Size of the array
arr = [1, 2, 3, 4, 5]  # Original array



rotate_left(arr,n)

rotate_left_opt(arr,n)

rotate_left(arr,n)