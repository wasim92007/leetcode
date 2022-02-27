class Solution:
    def search(self, nums: List[int], target: int) -> int:

        ## Algorithm, we will try to cast the problem into 
        ## parts/subcases so that we can perfor binary-search
        ## on sone specific portion

        ##  The shape of the array will be a saw tooth.

        ## Initialize
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r-l+1)//2

            if target == nums[m]:
                return m

            ## Check if the middle is in left sorted portion:
            if nums[l] <= nums[m]:
                ## Check to see if the target is on the right of 
                ## the middle
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1

            ## The middle is in the right portion
            else:
                ## Check to see if the target is on the left of 
                ## the middle
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
                    
        return -1
