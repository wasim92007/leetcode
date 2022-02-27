#
# @lc app=leetcode id=33 lang=python3
#
# [ 33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (37.41%)
# Likes:    12782
# Dislikes: 845
# Total Accepted:    1.4M
# Total Submissions: 3.6M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# There is an integer array nums sorted in ascending order (with distinct
# values).
# 
# Prior to being passed to your function, nums is possibly rotated at an
# unknown pivot index k (1 <= k < nums.length) such that the resulting array is
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
# (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3
# and become [4,5,6,7,0,1,2].
# 
# Given the array nums after the possible rotation and an integer target,
# return the index of target if it is in nums, or -1 if it is not in nums.
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# 
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
# Input: nums = [1], target = 0
# Output: -1
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -10^4 <= target <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        ## Algorithm, we will try to cast the problem into 
        ## parts/subcases so that we can perfor binary-search
        ## on sone specific portion

        ##  The shape of the array will be a saw tooth.

        ## Initialize
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r-l+1)//2

            if target == nums[m]:
                return m

            ## Check if the middle is in left sorted portion:
            if nums[l] <= nums[m]:
                ## Check to see if the target is on the right of 
                ## the middle
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1

            ## The middle is in the right portion
            else:
                ## Check to see if the target is on the left of 
                ## the middle
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
                    
        return -1

        
# @lc code=end

