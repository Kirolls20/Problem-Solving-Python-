class Solution:
     def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0   
        for i in range(len(items)):
            if ruleKey == 'type' and  items[i][0] == ruleValue:
                count+=1
            elif ruleKey == 'color' and items[i][1] == ruleValue:
                count+=1
            elif ruleKey == 'name' and items[i][2] == ruleValue:
                count+=1
        return count
obj = Solution()
print(obj.countMatches( [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"))
# https://leetcode.com/problems/count-items-matching-a-rule/description/