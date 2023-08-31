class Solution:
    """
    Input: command = "G()(al)"
    Output: "Goal"
    Explanation: The Goal Parser interprets the command as follows:
    G -> G
    () -> o
    (al) -> al
    The final concatenated result is "Goal".
    """
    def interpret(self, command: str) -> str:
        s = command.replace('()','o')
        new_s = s.replace('(al)','al')
        return new_s
        
        
       
        
obj = Solution()
print(obj.interpret('G()()()()(al)'))
#https://leetcode.com/problems/goal-parser-interpretation/description/