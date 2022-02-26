#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (32.80%)
# Likes:    21584
# Dislikes: 963
# Total Accepted:    3M
# Total Submissions: 9.2M
# Testcase Example:  '"abcabcbb"'
#
# Given a string s, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# 
# 
# Example 2:
# 
# 
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# Example 3:
# 
# 
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        ## Algorithm:
        ## Leetcode: https://www.youtube.com/watch?v=wiGpQwVHdE0
        ## We will have a sliding two pointer approch. We will
        ## keep on incrementing the right pointer till we hit 
        ## the end. We will increment left pointer till we have
        ## only unique characters.

        ans, lp = 0, 0
        char_set = set()

        ## We will keep incrementing the right pointer rp using
        ## this for loop
        for rp in range(len(s)):
            ## If the new incremented char is in char set, we
            ## will keep on removing element from the left till
            ## we have only unique character.
            while s[rp] in char_set:
                ## Remove character
                char_set.remove(s[lp])
                ## Increment the left pointer lp
                lp += 1

            ## Add the new charater to the set
            char_set.add(s[rp])
            ## Update our answer
            ans = max(ans, rp-lp+1) ## +1 when rp=lp

        return ans




        
# @lc code=end

