from typing import List

class Solution:
    def two_sum_bf(self,nums:List[int],target:int)-> List[int] :
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] + nums[j] == target :
                    return [i,j]
        
        return [-1, -1]
    
    def sum_of_two(self,nums:List[int],target:int)-> List[int] :
        n = len(nums)
        map = {}
        for ind,val in enumerate(nums):
            curr = target - val

            if curr in map :
                return [map[curr],ind]
            
            map[val] = ind
        
        return [ -1, -1]
     
if __name__ == '__main__':
    sol = Solution()
    arr = [22, 3, 1, 6, 9, 12]
    target = 7
    print(sol.two_sum_bf(arr,target))
    print(sol.sum_of_two(arr,10))