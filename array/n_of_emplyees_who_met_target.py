class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: list[int], target: int) -> int:
        count= 0 
        for i in hours:
            if i >= target:
                count +=1
        return count
    
obj = Solution
myobj = obj.numberOfEmployeesWhoMetTarget(obj,[1,2,3,4,5],3)
print(myobj)
