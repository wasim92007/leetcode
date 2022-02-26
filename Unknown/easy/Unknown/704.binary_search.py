#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#
# https://leetcode.com/problems/binary-search/description/
#
# algorithms
# Easy (54.63%)
# Likes:    3568
# Dislikes: 92
# Total Accepted:    666.7K
# Total Submissions: 1.2M
# Testcase Example:  '[-1,0,3,5,9,12]\n9'
#
# Given an array of integers nums which is sorted in ascending order, and an
# integer target, write a function to search target in nums. If target exists,
# then return its index. Otherwise, return -1.
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# 
# 
# Example 2:
# 
# 
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -10^4 < nums[i], target < 10^4
# All the integers in nums are unique.
# nums is sorted in ascending order.
# 
# 
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1

        ## Alternative faster solution: Tries to return the
        ## left point
        while l < r:
            m = l + (r-l+1)//2  ## Mid will co-inside with r for n =2
            #print(f'l:{l}, m:{m}, r:{r}')

            if target < nums[m]:
                r = m -1
            else:
                l = m
        
        return l if nums[l] == target else -1



        ## My First Solution: I try to return the mid point
        ## We will searchin the range
        ## l = r: Takes care of single element array
        while l <= r:
            m = (l+r)//2 ## Mid will co-inside with l for n = 2

            ## We will always check and return mid point
            if nums[m] == target:
                return m
            ## Already checked mid point, serach rigth if the target is more
            elif target > nums[m]:
                l = m+1
            else:
                r = m -1
        ## We searched entire range and came here means we could not find.
        return - 1

        
# @lc code=end

