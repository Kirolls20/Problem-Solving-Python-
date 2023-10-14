class Solution:
    """
    Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
    That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
    
    Input: nums = [8,1,2,2,3]
    Output: [4,0,1,1,3]


    """
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        ans = []
        inc = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    inc += 1
            ans.append(inc)
            inc=0
        return ans
obj = Solution()
print(obj.smallerNumbersThanCurrent([8,1,2,2,3])) #output [4,0,1,1,3]
            
