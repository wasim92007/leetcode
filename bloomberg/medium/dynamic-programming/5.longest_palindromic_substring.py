#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (31.67%)
# Likes:    16123
# Dislikes: 951
# Total Accepted:    1.7M
# Total Submissions: 5.4M
# Testcase Example:  '"babad"'
#
# Given a string s, return the longest palindromic substring in s.
# 
# 
# Example 1:
# 
# 
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: s = "cbbd"
# Output: "bb"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s consist of only digits and English letters.
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:

        ## Algorithm:
        ## https://www.youtube.com/watch?v=XYQecbcd6_c
        ## Here we will start from a character and move to the
        ## left and right and keep on updating the result and count

        ans = ''
        max_len = 0
        for i in range(len(s)):

            ## Check the odd case:
            ##  Initialize both left pointer lp and right pointer rp
            ## to i.
            lp, rp = i, i

            ## Keep moving the lp and rp as long as they are in bound
            while lp >= 0 and rp < len(s) and s[lp] == s[rp]:
                ## Update result if new max_len is found
                if rp - lp + 1 > max_len:
                    ans = s[lp:rp+1]
                    max_len = rp - lp + 1
                ## Move the pointers
                lp -= 1; rp += 1

            ## Check the even case: (It is a corner case actually)
            ##  Initialize left pointer lp and right pointer rp
            ## to i and i+1
            lp, rp = i, i+1

            ## Keep moving the lp and rp as long as they are in bound
            while lp >= 0 and rp < len(s) and s[lp] == s[rp]:
                ## Update result if new max_len is found
                if rp - lp + 1 > max_len:
                    ans = s[lp:rp+1]
                    max_len = rp - lp + 1
                ## Move the pointers
                lp -= 1; rp += 1

        return ans
        
# @lc code=end

