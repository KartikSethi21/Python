# Brute Force
def largest_elem_BF(arr):
    max = arr[-1]
    print(max)

# Optimal Approach
def largest_elem(arr):
    if len(arr) >0 :
        maxi = float("-inf")
        for i in arr:
            if i > maxi: maxi = i
    
        print(maxi)



arr = [2,33,43,65,13,1,90]
largest_elem_BF(arr)
largest_elem(arr)