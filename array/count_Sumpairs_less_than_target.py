class Solution:
    """
    Given a 0-indexed integer array nums of length n and an integer target, 
    return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.
    """
    def countPairs(self,nums:list[int],target:int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if 0 <= i < j < len(nums) and nums[i] + nums[j] < target:
                    count+=1
        return count
    
obj = Solution()
print(obj.countPairs([-6,2,5,-2,-7,-1,3],-2))

# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/