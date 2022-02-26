#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
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

        ## Algorithm:
        ## If the array is rotated by the target item tend to move
        ## right and values higher than the target seems to come 
        ## towards left.
        ##

        ## Initialize the left and right pointer
        lp, rp = 0, len(nums) - 1

        while lp <= rp:
            mp = (lp + rp) // 2
            print(f'lp:{lp}, mp:{mp}, rp:{rp}')
            if nums[mp] == target:
                return mp

            ## if the target is higher than the left most point
            ## --> Normal binary search as usual
            if target >= nums[lp]:
                print(f'Inside if 1')
                if target > nums[mp]:
                    lp = mp + 1
                else:
                    rp = mp - 1

            ## if target is less than the left most point, the array has
            ## and we need to compare with mid point to take further decision
            else:
                print(f'Inside if 1 else')
                ## In this case the binary search will be as usual
                if target < nums[rp]:
                    lp = mp + 1
                else:
                    rp = mp - 1
            print(f'after lp:{lp}, mp:{mp}, rp:{rp}')


        
# @lc code=end
