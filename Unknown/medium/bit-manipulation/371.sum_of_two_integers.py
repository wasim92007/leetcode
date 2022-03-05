#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#
# https://leetcode.com/problems/sum-of-two-integers/description/
#
# algorithms
# Medium (50.66%)
# Likes:    2355
# Dislikes: 3551
# Total Accepted:    281.6K
# Total Submissions: 556.1K
# Testcase Example:  '1\n2'
#
# Given two integers a and b, return the sum of the two integers without using
# the operators + and -.
# 
# 
# Example 1:
# Input: a = 1, b = 2
# Output: 3
# Example 2:
# Input: a = 2, b = 3
# Output: 5
# 
# 
# Constraints:
# 
# 
# -1000 <= a, b <= 1000
# 
# 
#

# @lc code=start


class Solution:
    def getSum(self, a: int, b: int) -> int:

        ## Algorithm: We will do xor followed by add with shifted and
        ## https://www.youtube.com/watch?v=k5qkqYL3bgg
        
        ## Python does not have signed binary representation
        if a < b:
            return self.getSum(b, a)
        
        x, y = abs(a), abs(b)

        sign = 1
        if a <= 0:  ## = sign needed for case -1, 0
            sign = -1

        if a*b >= 0: ## Either both negative or positive or zero
            ## Addition of x, y
            while y:
                xor = x^y
                carry = (x&y) << 1
                x, y = xor, carry

        else: ## Assuming only y is negative
            ## Subtraction: x - y
            while y:
                xor = x^y
                carry = (~x&y) << 1
                x, y = xor, carry

        return sign * x

        
# @lc code=end

