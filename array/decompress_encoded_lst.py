class Solution:
    """
    Example:

    Input: nums = [1,2,3,4]
    Output: [2,4,4,4]
    Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
    The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
    At the end the concatenation [2] + [4,4,4] is [2,4,4,4].
    """
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        lst =[]
        for i in range(0,len(nums),2):
            frq= nums[i]
            val = nums[i+1]
            lst +=[val]*frq
        return lst
obj = Solution()
print(obj.decompressRLElist([1,1,2,3]))
# https://leetcode.com/problems/decompress-run-length-encoded-list/description/