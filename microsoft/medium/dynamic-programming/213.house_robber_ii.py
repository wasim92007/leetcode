#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#
# https://leetcode.com/problems/house-robber-ii/description/
#
# algorithms
# Medium (39.44%)
# Likes:    4776
# Dislikes: 84
# Total Accepted:    351.2K
# Total Submissions: 890.1K
# Testcase Example:  '[2,3,2]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed. All houses at this place are
# arranged in a circle. That means the first house is the neighbor of the last
# one. Meanwhile, adjacent houses have a security system connected, and it will
# automatically contact the police if two adjacent houses were broken into on
# the same night.
# 
# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the
# police.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money =
# 2), because they are adjacent houses.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2,3]
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000
# 
# 
#

# @lc code=start


class Solution:
    def rob(self, nums: List[int]) -> int:

        ## Get the length first
        l = len(nums)

        ## In case of circular for l <=3
        ## We can only rob one house
        if l <= 3:
            return max(nums)

        ## Algorithm: We will break the circular dependency
        ## by taking two over-lapping array and getting the max
        ## of both
        ## https://www.youtube.com/watch?v=rWAJCfYYOvM
        return max(self.rob_non_circular(nums=nums[:-1]), self.rob_non_circular(nums=nums[1:]))

    def rob_non_circular(self, nums: List[int]) -> int:
        ## Will be used to keep track of the max value till
        ## 2nd last houst and last house.
        till_2nd_last, till_last = 0, 0

        ## Algorithm: The max value at the current house will
        ## be maximum of till_2nd_last plus value at current 
        ## house, till_last house
        for num in nums:
            till_curr = max(till_2nd_last + num, till_last)

            ## Shift one to the rigt for next iteration
            till_2nd_last, till_last = till_last, till_curr

        ## At the end of the loop the till_last will be the till_curr
        return till_last
        
# @lc code=end

