class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        l = len(nums)
        
        r = 0
        for n in nums:
            r = r ^ n
            
        return r
