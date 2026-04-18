def findMaxConsecutiveOnes(arr):
    cnt, maxi = 0, 0

    for num in arr:
        if num == 1:
            cnt+=1
        else:
            cnt = 0
        maxi = max(maxi,cnt)

    print(maxi)

arr = [1,1,1,1,0,0,11,1,1,4,3]
findMaxConsecutiveOnes(arr)