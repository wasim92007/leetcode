#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (30.55%)
# Likes:    16213
# Dislikes: 1552
# Total Accepted:    1.8M
# Total Submissions: 5.8M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an integer array nums, return all the triplets [nums[i], nums[j],
# nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] +
# nums[k] == 0.
# 
# Notice that the solution set must not contain duplicate triplets.
# 
# 
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:
# Input: nums = []
# Output: []
# Example 3:
# Input: nums = [0]
# Output: []
# 
# 
# Constraints:
# 
# 
# 0 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
# 
# 
#

# @lc code=start


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ## Algorithm: 1. We will first sort the array to avoid duplicates
        ##            2. We will select the first element and for rest of
        ##               the sum we will use 2 sum version 2 method
        ## https://www.youtube.com/watch?v=jzZsG8n2R9A

        ## Placeholder
        res = []
        ## Sorting
        nums.sort()

        for i, a in enumerate(nums):
            ## Avoid duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums) - 1
            ## Two sum with offset
            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1

                    ## We will exploit all the other possible b, c combination using
                    ## the below while loop
                    ## We will keep a check for duplicate as well as bound
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif threesum > 0:
                    r -= 1
                else:
                    l += 1

        return res

        
# @lc code=end

