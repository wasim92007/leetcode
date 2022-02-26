class Solution:
    def hammingWeight(self, n: int) -> int:
        
        hw = 0
        while n:
            hw += n & 1 ## Sampling last bit
            n = n >> 1
            
        return hw
