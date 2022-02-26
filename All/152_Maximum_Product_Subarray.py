class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ## This problem is a trciky problem
        ## https://www.youtube.com/watch?v=lXVy6YWFcRM
        ## Here we not only just need to keep track of the max but also the mix
        
        ## Lets us intialize out max_prod_subarr to max of the array
        max_prod_subarr = max(nums) # Can  not set it to 0 as not true for nums = [-1]
        
        ## Initialize curr_max and curr_min to 1
        curr_max, curr_min = 1, 1
        
        for n in nums:
            ## Update curr_max, curr_min
            old_max = curr_max ## We need to do this as this will be used for curr_min calculation
            curr_max = max(n*curr_max, n*curr_min, n) ## n will also be included for nums = [-1, 8]
            curr_min = min(n*old_max, n*curr_min, n)
            
            ## Update the max_prod_subarr
            max_prod_subarr = max(max_prod_subarr, curr_min, curr_max)
                
        return max_prod_subarr
