class Solution:
    """
    Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
    Return the running sum of nums.
    
    Input: nums = [1,2,3,4]
    Output: [1,3,6,10] -> [1,1+2,1+2+3,1+2+3+4]
    """
    def runningSum(self,nums:list[int]) -> list[int]:
        lst= []
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            lst.append(count)
        return lst

        


obj = Solution()
print(obj.runningSum([1,1,1,1,1]))  # Output [1,2,3,4,5]