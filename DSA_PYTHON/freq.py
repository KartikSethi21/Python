
array = [ 1,2,3,33,33,2,1,4,4,4,5,2,1,2 ]

freq = {}

for num in array :
    if num in freq:
        freq[num] +=1
    else:
        freq[num] = 1
    
print(freq)


freq1 = {}

for num in array:
    freq1[num] = freq1.get(num, 0) + 1

print(freq1)

# BRUTE FORCE APPROACH

def freq(arr, n):
    visited = [False] * n
    # print(visited)
    for i in range(n):
        if visited[i]:
            continue
        count = 1
        for j in range(i+1,n):
            if arr[i] == arr[j]:
                count+=1
                visited[j] = True
        print(arr[i],count)
    # print(visited)

freq(array,len(array))

# print(array)    
# print(len(array))
