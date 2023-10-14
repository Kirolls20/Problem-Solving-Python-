class Solution:
    """
    You are given a positive integer array nums.

    -The element sum is the sum of all the elements in nums.
    -The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
        Return the absolute difference between the element sum and digit sum of nums.

    *Note that the absolute difference between two integers x and y is defined as |x - y|.
    
    """
    def differenceOfSum(self, nums: list[int]) -> int:
        sum1= sum(nums)
        num_of_digits= ''
        for x in nums:
            num_of_digits+=str(x)
        
        sum2= 0 
        for i in num_of_digits:
            sum2+=int(i)
        result= abs(sum1 - sum2)
        return result
        

obj = Solution()
print(obj.differenceOfSum([1,15,6,3]))
# The Problem in Leetcode 
# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/
