class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1

        ## We will searchin the range
        ## l = r: Takes care of single element array
        while l <= r:
            m = (l+r)//2

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
        
