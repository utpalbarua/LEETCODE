class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        res=[]
        x=0

        for i in nums:
            x+=i
            res.append(x)
            
        return res