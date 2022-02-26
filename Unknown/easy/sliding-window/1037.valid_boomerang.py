#
# @lc app=leetcode id=1037 lang=python3
#
# [1037] Valid Boomerang
#
# https://leetcode.com/problems/valid-boomerang/description/
#
# algorithms
# Easy (37.47%)
# Likes:    216
# Dislikes: 341
# Total Accepted:    29.9K
# Total Submissions: 79.9K
# Testcase Example:  '[[1,1],[2,3],[3,2]]'
#
# Given an array points where points[i] = [xi, yi] represents a point on the
# X-Y plane, return true if these points are a boomerang.
# 
# A boomerang is a set of three points that are all distinct and not in a
# straight line.
# 
# 
# Example 1:
# Input: points = [[1,1],[2,3],[3,2]]
# Output: true
# Example 2:
# Input: points = [[1,1],[2,2],[3,3]]
# Output: false
# 
# 
# Constraints:
# 
# 
# points.length == 3
# points[i].length == 2
# 0 <= xi, yi <= 100
# 
# 
#

# @lc code=start
class Solution:
    ## Algorithm:
    ## We will be using triangle inequality: The sum of any two sides
    ## in a triangle is greater than the third side.
    ## **We need to check this inequality for all 3 sides.
    ## Unfortunately ab < ac + bc is giving wrong value due to approximation
    ## Unfortunately ab == ac + bc is giving wrong value due to approximation
    ## Calculating m may cause divide by 0 error.

    def distance(self, p1, p2):
        return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

    def isBoomerang(self, points: List[List[int]]) -> bool:
        def d(p1, p2):
            dy = p1[1] - p2[1]
            dx = p1[0] - p2[0]
            
            try:
                return dy / dx
            except:
                return 0
            
        p = points
        if len(set([str(x) for x in p])) == 2:
            return False
        
        if p[0][0] == p[1][0] == p[2][0]:
            return False
        
        if p[0][1] == p[1][1] == p[2][1]:
            return False
        
        d1 = d(p[0], p[1])
        d2 = d(p[1], p[2])
        if d1 == 0 or d2 == 0:
            return True
        
        return d1 != d2   

        
        
# @lc code=end

