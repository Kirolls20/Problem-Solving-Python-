class Solution:
    """
    You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:

    -i < j < k,
    -nums[j] - nums[i] == diff, and
    -nums[k] - nums[j] == diff.
        Return the number of unique arithmetic triplets
    
    """
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        count =0 
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                for k in range(j,len(nums)):
                    if (nums[j] - nums[i] == diff) and (nums[k] - nums[j] == diff) :
                        count+=1
        return count

obj = Solution()
print(obj.arithmeticTriplets(nums = [0,1,4,6,7,10], diff = 3))   
print(obj.arithmeticTriplets( [4,5,6,7,8,9], diff = 2))
# The ProblemSet in LeetCode 
#https://leetcode.com/problems/number-of-arithmetic-triplets/description/