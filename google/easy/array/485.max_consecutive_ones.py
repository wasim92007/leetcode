#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#
# https://leetcode.com/problems/max-consecutive-ones/description/
#
# algorithms
# Easy (54.80%)
# Likes:    2617
# Dislikes: 396
# Total Accepted:    653K
# Total Submissions: 1.2M
# Testcase Example:  '[1,1,0,1,1,1]'
#
# Given a binary array nums, return the maximum number of consecutive 1's in
# the array.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive
# 1s. The maximum number of consecutive 1s is 3.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,0,1,1,0,1]
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1.
# 
# 
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ## The startegy here is to keep a running sum
        ## with the trick that we will restart once we encounter a 0.
        ## Restart is done by multipyting the running sum with
        ## the current element
        curr_max = 0
        max_one  = 0
        for n in nums:
            curr_max = curr_max*n + n
            if curr_max > max_one:
                max_one = curr_max

        return max_one
        
# @lc code=end

