class Solution:
    '''
        there is a programming language with only four operations and one variable X:
        ++X and X++ increments the value of the variable X by 1.
        --X and X-- decrements the value of the variable X by 1.
    
    '''
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        x = 0
        for i in operations:
            if i in ('++X','X++'):
                x+=1
            elif i in ('--X','X--'):
                x-=1
        return x

obj = Solution()
myobj = obj.finalValueAfterOperations(["++X","++X","X++"])
print(myobj)