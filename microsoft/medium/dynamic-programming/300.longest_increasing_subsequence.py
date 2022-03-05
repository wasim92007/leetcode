#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (48.51%)
# Likes:    10948
# Dislikes: 215
# Total Accepted:    791.1K
# Total Submissions: 1.6M
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# Given an integer array nums, return the length of the longest strictly
# increasing subsequence.
# 
# A subsequence is a sequence that can be derived from an array by deleting
# some or no elements without changing the order of the remaining elements. For
# example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
# 
# 
# Example 1:
# 
# 
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
# length is 4.
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,1,0,3,2,3]
# Output: 4
# 
# 
# Example 3:
# 
# 
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 2500
# -10^4 <= nums[i] <= 10^4
# 
# 
# 
# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time
# complexity?
# 
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ## Algorithm: The idea here is to start from the right and
        ## use dp
        ## https://www.youtube.com/watch?v=cjWnW0hdF1Y

        l = len(nums)
        LIS = [1]*l

        ## We will start from the last element
        for i in range(l-1, -1, -1):
            ## When in the middle, we will check for the subseqent
            for j in range(i+1, l):
                ## We will consider if the next element is higher than
                ## the current element
                if nums[j] > nums[i]:
                    ## We are doing 1 + LIS[j] because we are doing longest substring
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)
        
# @lc code=end

