
class Solution:
    ''' 
Description 
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn].

'''
  
    def shuffle(self, nums: list[int], half: int) -> list[int]:
        half= len(nums) // 2
        lst1 = nums[:half]
        lst2 = nums[half:]
        shuffled_list = []
        for i in range(len(lst1)):
            shuffled_list.append(lst1[i])
            shuffled_list.append(lst2[i])          
        return shuffled_list

obj = Solution()
myobj = obj.shuffle([1,2,3,4,5,6,7,8],3)  # [1,4,2,5,3,6]
print(myobj)