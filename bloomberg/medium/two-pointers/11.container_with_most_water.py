#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (53.37%)
# Likes:    14535
# Dislikes: 874
# Total Accepted:    1.3M
# Total Submissions: 2.5M
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# You are given an integer array height of length n. There are n vertical lines
# drawn such that the two endpoints of the i^th line are (i, 0) and (i,
# height[i]).
# 
# Find two lines that together with the x-axis form a container, such that the
# container contains the most water.
# 
# Return the maximum amount of water a container can store.
# 
# Notice that you may not slant the container.
# 
# 
# Example 1:
# 
# 
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array
# [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the
# container can contain is 49.
# 
# 
# Example 2:
# 
# 
# Input: height = [1,1]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# n == height.length
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4
# 
# 
#

# @lc code=start


class Solution:
    def maxArea(self, height: List[int]) -> int:

        ### Algorithm: Brite force solution
        ### Time Limit Exceeded Error
        ### Check every pair of container
        #area = 0
        #for lp in range(len(height)):
        #    ## Set rp to the immediate next point
        #    rp = lp + 1
        #    ## As long as rp is in bound
        #    for rp in range(lp+1,len(height)):
        #        ## Get the new area
        #        new_area = (rp-lp) * min(height[lp], height[rp])
        #        ## Update the old are if required
        #        if new_area > area:
        #            area = new_area

        #return area

        ## Alogorithm
        ## https://www.youtube.com/watch?v=UuiTKBwPgAo
        ## Kind of greedy algorithm.
        ## Start with left and right pointer initialized to the
        ## Extreme left and right and try to maximize the height
        lp, rp = 0, len(height) - 1
        area = 0
        while lp != rp:
            ## Update new area
            area = max(area, (rp-lp)*min(height[lp], height[rp]))
            if height[lp] < height[rp]:
                lp += 1
            else:
                rp -= 1

        return area
        
# @lc code=end

