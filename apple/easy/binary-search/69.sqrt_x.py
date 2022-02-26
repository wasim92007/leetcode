#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (36.24%)
# Likes:    3379
# Dislikes: 3026
# Total Accepted:    961.2K
# Total Submissions: 2.6M
# Testcase Example:  '4'
#
# Given a non-negative integer x, compute and return the square root of x.
# 
# Since the return type is an integer, the decimal digits are truncated, and
# only the integer part of the result is returned.
# 
# Note: You are not allowed to use any built-in exponent function or operator,
# such as pow(x, 0.5) or x ** 0.5.
# 
# 
# Example 1:
# 
# 
# Input: x = 4
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part
# is truncated, 2 is returned.
# 
# 
# Constraints:
# 
# 
# 0 <= x <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x <= 1:
            return x
        
        ## Initialization of the binary search
        l = 1; r = x//2
        
        while l < r:
            ## We will choose mid point such the it co-incides with r
            ## for n = 1
            m = l + (r-l+1)//2
            
            ## We will check if target is in left side first
            ## No equal checking required as we will coincide
            ## this will the l
            if x < m*m:
                r = m - 1
            else:
                l = m
        
        return l
        
        
# @lc code=end

