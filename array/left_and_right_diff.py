class Solution:
    """
    given a 0-indexed integer array nums, find a 0-indexed integer array answer where:
    answer.length == nums.length.
    answer[i] = |leftSum[i] - rightSum[i]|.
    Where:

    leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
    rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
    Return the array answer.
    """
    def leftRightDifference(self,nums:list[int]) -> list[int]:
        # initilizing list of zeros
        leftSum = [0] * len(nums)
        rightSum = [0] * len(nums)

        running_sum = 0
        # Left Side loop
        for i in range(len(nums)):
            running_sum+=nums[i]
            leftSum[i] = running_sum
        running_sum = 0 
        # right Side loop
        for i in range(len(nums) -1,-1,-1):
            running_sum+= nums[i]
            rightSum[i] = running_sum
    
        answer = [abs(leftSum[i] - rightSum[i]) for i in range(len(nums))]
        return answer
obj = Solution()
print(obj.leftRightDifference([10,4,8,3])) # Output: [15,1,11,22]
# https://leetcode.com/problems/left-and-right-sum-differences/