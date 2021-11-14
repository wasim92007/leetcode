class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        ## https://www.youtube.com/watch?v=eqX3WZGpma4
        count = 1
        m_ele = nums[0]
        
        for ele in nums[1:]:
            if ele == m_ele:
                count += 1
            else:
                count -= 1
                if count == 0:
                    m_ele = ele
                    count += 1
                    
        return m_ele
        
        
        ## Using in-built counter function
        ## My method
        from collections import Counter
        
        c = Counter(nums)
        
        return c.most_common(1)[0][0]
