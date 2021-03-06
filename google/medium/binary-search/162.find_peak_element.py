#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#
# https://leetcode.com/problems/find-peak-element/description/
#
# algorithms
# Medium (45.60%)
# Likes:    5412
# Dislikes: 3534
# Total Accepted:    722.5K
# Total Submissions: 1.6M
# Testcase Example:  '[1,2,3,1]'
#
# A peak element is an element that is strictly greater than its neighbors.
# 
# Given an integer array nums, find a peak element, and return its index. If
# the array contains multiple peaks, return the index to any of the peaks.
# 
# You may imagine that nums[-1] = nums[n] = -∞.
# 
# You must write an algorithm that runs in O(log n) time.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index
# number 2.
# 
# Example 2:
# 
# 
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak
# element is 2, or index number 5 where the peak element is 6.
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 1000
# -2^31 <= nums[i] <= 2^31 - 1
# nums[i] != nums[i + 1] for all valid i.
# 
# 
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        l = len(nums)
        lp, rp = 0 , l -1

        while lp <= rp:
            ## Find the middle point
            m = lp + (rp-lp+1)//2
            ##Check if mid is not at the extreme end
            if m > 0 and m < l - 1:
                if nums[m] > nums[m-1] and nums[m] > nums[m+1]:
                    return m
                else:
                    if nums[m-1] < nums[m]:
                        l = m 
                    else:
                        r = m
            else:
                if m == 0:
                    if nums[m] > nums[m+1]:
                        return m
                    else:
                        return 1
                elif m == l -1:
                    if nums[m] > nums[m-1]:
                        return m
                    else:
                        return m - 1




        
# @lc code=end

