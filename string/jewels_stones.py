class Solution:
    """
    You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. 
    Each character in stones is a type of stone you have. 
    You want to know how many of the stones you have are also jewels.

    Input: jewels = "aA", stones = "aAAbbbb"
    Output: 3
    """
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count =0 
        s = list(stones)
        for i in range(len(s)):
            if stones[i] in jewels:
                count+=1
        return count 
    
obj =Solution()
print(obj.numJewelsInStones('z','ZZ'))
# https://leetcode.com/problems/jewels-and-stones/description/
