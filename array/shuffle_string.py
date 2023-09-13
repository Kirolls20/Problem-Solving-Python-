class Solution:
    '''
    You are given a string s and an integer array indices of the same length. 
    The string s will be shuffled such that the character at the ith position
    moves to indices[i] in the shuffled string.
    Return the shuffled string.
    
    '''
    def restoreString(self, s: str, indices: list[int]) -> str:
        lst = [""] * len(s)
        for i in range(len(s)):
            lst[indices[i]] = s[i]
        return "".join(lst)
            
     

obj = Solution()
x= obj.restoreString('codeleet',[4,5,6,7,0,2,1,3]) # leetcode
print(x)
# https://leetcode.com/problems/shuffle-string/description/