# Using map
#  T.C - O((n+m) log(n+m)) => O(n+m) for looping and getting freq and log(n+m) for sorting
#  S.C O(n+m) => storing freq

def union_map(arr1, arr2, n, m):
    freq = {}

    for i in range(n):
        num = arr1[i]
        if num in freq:
            freq[num]+=1
        else:
            freq[num] = 1
        
        # freq[num] = freq.get(num,0)+1
    for i in range(m):
        num = arr2[i]
        if num in freq:
            freq[num]+=1
        else:
            freq[num] = 1
        
        # freq[num] = freq.get(num,0)+1
    # print(freq)
    
    Union = sorted(freq.keys())
    return Union

#  T.C - O((n+m) log(n+m)) => 
#  S.C - O(n+m) => storing the output

# sorted => converts set to sorted list
def union_set(arr1, arr2, n, m):
    st = set(arr1) | set(arr2)

    return sorted(st)


#  T.C - O(n+m) 
#  S.C - O(n+m) => storing the output

def union_opt(arr1, arr2, n ,m):
    i , j =0 ,0
    union = []

    while i<n and j<m:
        num1, num2 = arr1[i], arr2[j]
        if num1 <num2:
            if not union or union[-1] != num1:
                union.append(num1)
            i+=1
        elif num2 < num1 :
            if not union or union[-1] != num2:
                union.append(num2)
            j+=1
        else:
            if not union or union[-1] != num1:
                union.append(num1)
            i+=1
            j+=1
    
    while i < n:
        num1 = arr1[i]
        if not union or union[-1]  != num1:
            union.append(num1)
        i+=1    
    while j < m:
        num2 = arr2[j]
        if not union or union[-1]  != num2:
            union.append(num2)
        j+=1

    return union

            


n = 10
# Define size of second array
m = 7
# Initialize first array
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Initialize second array
arr2 = [2, 3, 4, 4, 5, 11, 12]
arr = union_map(arr1, arr2, n, m)
print(arr[:])

arr = union_set(arr1, arr2, n, m)
print(arr[:])

arr = union_opt(arr1, arr2, n, m)
print(arr[:])
