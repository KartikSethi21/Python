# T.C - O(N)
# T.C - O(1)

def sec_largest_elem(arr):
    maxi = sec_maxi = float("-inf") 
    for i in arr:
        if i > maxi :
            sec_maxi = maxi
            maxi = i
        if i > sec_maxi and i <maxi :
            sec_maxi = i

    print("Largest Element In Array is",maxi)
    print("Second Largest Element In Array is",sec_maxi)
            
    
def sec_smallest_elem(arr):
    mini = sec_mini = float("inf") 
    for i in arr:
        if i < mini :
            sec_mini = mini
            mini = i
        if i < sec_mini and i >mini :
            sec_mini = i

    print("Smallest Element In Array is",mini)
    print("Second Smallest Element In Array is",sec_mini)
            
    

arr = [1,22,32,11,44,66,44,23,98,66]
sec_largest_elem(arr)
sec_smallest_elem(arr)