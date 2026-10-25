class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:

        res=[]

        for i in accounts:
            x = sum(i)
            res.append(x)

        return max(res)

        