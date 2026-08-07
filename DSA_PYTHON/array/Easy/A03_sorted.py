from typing import List


def is_sorted(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[j] < arr[i]:
                return False
    return True

def is_sorted_opt(arr):
    n = len(arr)
    for i in range(1,n):
        if arr[i] < arr[i-1]:
            return False
    
    return True


arr = [1, 2, 6, 4, 5]

ts = is_sorted(arr)
ts2 = is_sorted_opt(arr)

print("Array is sorted",ts)
print("Array is sorted",ts2)


# 1,2,3,4,5   => +0
# 5,1,2,3,4   => +1
# 4,5,1,2,3   => +2
# 3,4,5,1,2   => +3
# 2,3,4,5,1   => +4
# 1,2,3,4,5   => +5 


def is_sorted_rotated(arr):
    n = len(arr)
    cnt =0
    for i in range(1,n):
        if arr[i] < arr[i-1]:
            cnt+=1
    print(cnt)
    if arr[n-1] >arr[0]:
        cnt+=1
    print(cnt)
    

    # return True if cnt==1 else False
    return cnt<=1


def is_sorted_rotated_mod(arr):
    n = len(arr)
    cnt = 0

    for i in range(n):
        if arr[i] > arr[(i + 1) % n]:
            cnt += 1

    return cnt <= 1


def check(self, nums: List[int]) -> bool:
    n=len(nums)
    count=0
    for i in range(1,n):
        if nums[i]<nums[i-1]:
            count+=1
    if nums[0]<nums[n-1]:
        count+=1
    return count<=1



    
arr = [5, 1, 2, 3, 4]
print("Is array rotated and sorted",is_sorted_rotated(arr))
arr =  [1, 2, 6, 4, 5]
print("Is array rotated and sorted",is_sorted_rotated_mod(arr))
arr=[5,4,3,2,1]
print(is_sorted_rotated(arr))
