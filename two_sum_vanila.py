class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        n = len(nums)
        for i, a in enumerate(nums):
            for j, b in enumerate(nums):
                if j > i and nums[i] + nums[j] == target:
                    return list([i,j])
