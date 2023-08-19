class Solution:
    '''Given an array of integers nums, return the number of good pairs.
        A pair (i, j) is called good if nums[i] == nums[j] and i < j.'''
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = 0 
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    count+=1            

        return count
    
obj = Solution()
print(obj.numIdenticalPairs([1,1,1,1])) # 6