class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        ## If n == 0: We do not need to do anything
        ## For n !=0: We have two subcases
        if n != 0:
            ## If m == 0, the we should place nums2 into nums1
            if m == 0:
                nums1[:n+1] = nums2
            ## General non zero case
            else:
                ## We we start filling from the end
                f = m + n - 1
                i = m
                j = n
                
                while i > 0 and j > 0:
                    if nums1[i-1] > nums2[j-1]:
                        nums1[f] = nums1[i-1]
                        i -= 1; f -= 1
                    else:
                        nums1[f] = nums2[j-1]
                        j -= 1; f -= 1
                        
                while j > 0:
                    nums1[f] = nums2[j-1]
                    j -= 1; f -=1
