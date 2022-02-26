#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (47.68%)
# Likes:    6061
# Dislikes: 372
# Total Accepted:    844.4K
# Total Submissions: 1.8M
# Testcase Example:  '[3,4,5,1,2]'
#
# Suppose an array of length n sorted in ascending order is rotated between 1
# and n times. For example, the array nums = [0,1,2,4,5,6,7] might
# become:
# 
# 
# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# 
# 
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results
# in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
# 
# Given the sorted rotated array nums of unique elements, return the minimum
# element of this array.
# 
# You must write an algorithm that runs in O(log n) time.
# 
# 
# Example 1:
# 
# 
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
# 
# 
# Example 2:
# 
# 
# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4
# times.
# 
# 
# Example 3:
# 
# 
# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4
# times. 
# 
# 
# 
# Constraints:
# 
# 
# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# All the integers of nums are unique.
# nums is sorted and rotated between 1 and n times.
# 
# 
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:

        ## Algorithm:
        ## https://www.youtube.com/watch?v=nIVW4P8b1VA
        ## Modified binary search.
        ## Invariance to idenify if we have rotated the array
        ## 1. lp value will alwayes be greater than rp value
        ## --> Will check if rotated or not
        ## 2. if roated by atleast half them the mid pointer will 
        ## always be greater than or equalt to the left-most(n=1)
        ## element. 
        ##  --> If we have rotated atleast half, we will search
        ##  the right portion else we will search the left portion

        lp, rp = 0, len(nums) - 1

        ## Very important: As out algorithm does not run for the
        ## non-ratated sorted array, we will take care of this by
        ## intializeing the result at left most value and update
        ##it after comparing
        res = nums[0]

        while lp <= rp:
            ## if already sorted then left most value will maybe
            ## the answer: Exception num_ = [2,3,4]
            ## Remember that our basic algorithm does not run on
            ## the non-roated sorted case
            if nums[lp] <= nums[rp]:
                res = min(res, nums[lp])
                break

            else:
                mp = (lp + rp) // 2
                ## As we ared discarding the mid point
                res = min(res, nums[mp])
                ## Search the right half
                if nums[mp] >= nums[lp]:
                    lp = mp + 1
                else:
                    rp = mp - 1
        return res
        
# @lc code=end

