class Solution:
    def decode(self,encoded:list[int],first:int) -> list[int]:
        arr = [first]
        for i in encoded:
            temp= i ^ first
            print(temp)
            arr.append(temp)
            first = temp
        return arr

obj= Solution()
print(obj.decode([1,2,3],1)) # Output: [1,0,2,1]
# https://leetcode.com/problems/decode-xored-array/description/

