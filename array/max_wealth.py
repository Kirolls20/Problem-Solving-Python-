class Solution:
    '''
        you are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. 
        Return the wealth that the richest customer has.
        A customer's wealth is the amount of money they have in all their bank accounts. 
        The richest customer is the customer that has the maximum wealth. 
        Exmple
        Input: accounts = [[1,5],[7,3],[3,5]]
        Output: 10
    
    '''
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        total_wealth= []
        for i in range(len(accounts)):
            total_wealth.append(sum(accounts[i]))
        return max(total_wealth)

obj = Solution()
print(obj.maximumWealth([[1,5],[7,3],[3,5]]))


