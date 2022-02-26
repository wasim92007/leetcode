#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (55.61%)
# Likes:    16847
# Dislikes: 239
# Total Accepted:    1M
# Total Submissions: 1.9M
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it can trap after raining.
# 
# 
# Example 1:
# 
# 
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array
# [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
# are being trapped.
# 
# 
# Example 2:
# 
# 
# Input: height = [4,2,0,3,2,5]
# Output: 9
# 
# 
# 
# Constraints:
# 
# 
# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        ## Algorithm: Two-pointer outward in greedy
        trapped_water = 0
        min_level = 0
        lp, rp = 0, len(height) - 1

        while lp != rp:
            ## If the min_level for trapping is higher that the lp and rp height
            ## Add the difference.
            trapped_water += max(0, min_level-height[lp]) + max(0, min_level-height[rp])
            ## Update min level for trapping to a higher both side bounded value
            min_level = max(min_level, min(height[lp], height[rp]))
            ## Greedily try to increase the height
            if height[lp] < height[rp]:
                lp += 1
            else:
                rp -= 1
                

        return trapped_water
        
# @lc code=end

