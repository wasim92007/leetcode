class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums = set(nums)
        
        l = len(nums)
        
        ## Remember that the for will go till l+1
        ## as per the problem definition
        for i in range(l+1):
            if i not in nums:
                return i
