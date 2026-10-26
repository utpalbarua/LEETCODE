class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:

        nums1 = set(nums)
        
        if len(nums) == len(nums1):
            return False
        else:
            return True
        