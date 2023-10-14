class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        lst = []
        maxi = max(candies)
        for candy in candies:
            if candy + extraCandies >= maxi:
                lst.append(True)
            else:
                lst.append(False)
    
        return lst
obj = Solution()
print(obj.kidsWithCandies([2,3,5,1,3],3)) # Output [true,true,true,false,true] 

        
    




            
            