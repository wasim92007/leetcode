#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
# https://leetcode.com/problems/house-robber/description/
#
# algorithms
# Medium (46.42%)
# Likes:    10980
# Dislikes: 241
# Total Accepted:    1M
# Total Submissions: 2.2M
# Testcase Example:  '[1,2,3,1]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security systems
# connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.
# 
# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the
# police.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5
# (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400
# 
# 
#

# @lc code=start
class Solution:

    def rob(self, nums: List[int]) -> int:
        l = len(nums)

        if l <= 2:
            return max(nums)

        ## Algorithm: dp[i] will store the max till 0->i
        dp = [0]*l

        dp[0] = nums[0]
        dp[1] = max(nums[:2])

        for i in range(2, l):
            dp[i] = max(nums[i] + dp[i-2],   ## Max till 2nd last house + Curr house
                        dp[i-1])             ## We will skip this house: 

        return dp[l-1]
        
# @lc code=end

