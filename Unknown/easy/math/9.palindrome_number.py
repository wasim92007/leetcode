#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (52.10%)
# Likes:    5246
# Dislikes: 2042
# Total Accepted:    1.9M
# Total Submissions: 3.6M
# Testcase Example:  '121'
#
# Given an integer x, return true if x is palindrome integer.
# 
# An integer is a palindrome when it reads the same backward as forward.
# 
# 
# For example, 121 is a palindrome while 123 is not.
# 
# 
# 
# Example 1:
# 
# 
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# 
# 
# Example 2:
# 
# 
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
# 
# 
# Example 3:
# 
# 
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a
# palindrome.
# 
# 
# 
# Constraints:
# 
# 
# -2^31 <= x <= 2^31 - 1
# 
# 
# 
# Follow up: Could you solve it without converting the integer to a string?
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        x_str = str(x)
        length = len(x_str)

        #if length == 1:
        #    return True

        if length % 2 == 0:
            l, r = length//2 - 1, length//2
        else:
            l, r = length//2 - 1, length//2 + 1

        while (l>=0) and (r<length):
            #print(f'l:{l}, r:{r}, l:{x_str[l]}, r:{x_str[r]}')
            if x_str[l] == x_str[r]:
                l -= 1; r += 1
            else:
                return False
        
        return True

        
# @lc code=end

