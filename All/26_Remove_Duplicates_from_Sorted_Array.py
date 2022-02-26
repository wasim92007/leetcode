class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen_list = {}

        l = len(nums) 
        
        ## Algorithm: Two pointer approach
        s, f = 0, 0
        seen_list = []
        while s < l and f < l:
            if nums[f] in seen_list:
                f += 1
            else:
                seen_list.append(nums[f])
                nums[s] = nums[f]
                s += 1; f += 1
                
        return s
                
