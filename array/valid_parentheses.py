class Solution(object):
    def isValid(self, s):
        stack = [] # only use append and pop
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)
            elif len(stack) == 0 or bracket != pairs[stack.pop()]:
                return False
        # it means return True if len ==0 if not ==0 return False
        return len(stack) == 0


obj= Solution()
o= obj.isValid('[{}])')
print(o)

[] 