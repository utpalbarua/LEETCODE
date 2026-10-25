class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:

        n = max(candies)
        res=[]

        for i in candies:
            if i + extraCandies >= n:
                res.append(True)
            else:
                res.append(False)
        return res
        