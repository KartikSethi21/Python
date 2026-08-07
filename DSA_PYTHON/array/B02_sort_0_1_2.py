
# First Approach
# O(n) 
# O(1)
def sort_array(arr):
    zero , one, two = 0, 0, 0
    n = len(arr)
    for num in arr:
        if num == 0:
            zero+=1
        elif num == 1:
            one += 1
        elif num == 2:
            two+= 1
    
    index = 0
    for _ in range(zero):
        arr[index] = 0
        index+=1
        
    for _ in range(one):
        arr[index] = 1
        index+=1
        
    for _ in range(two):
        arr[index] = 2
        index+=1

    print(arr[:])


# Second Approach
# O(n) 
# O(1)
def sort_array_better(arr):
    zero, one, two = 0, 0, 0
    for num in arr:
        if num == 0:
            zero+=1
        elif num == 1:
            one+=1
        else:
            two+=1
    
    for i in range(zero):
        arr[i] = 0
    for i in range(zero, zero+one):
        arr[i] = 1
    for i in range(zero+one, zero+one+two):
        arr[i] = 2
    
    print(arr[:])



# Third Approach => Dutch National Flag Algorithm
# O(n) 
# O(1)
def sort_array_opt(arr):
    low, mid, high = 0, 0, len(arr)-1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low+=1
            mid+=1
        elif arr[mid] == 1:
            mid+=1
        else:
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1
    
    print(arr[:])

arr = [1, 0, 2, 1, 0]
sort_array(arr)
arr = [1, 0, 2, 1, 0]
sort_array_better(arr)
arr = [1, 0, 2, 1, 0]
sort_array_opt(arr)
        

