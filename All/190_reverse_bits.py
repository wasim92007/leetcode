class Solution:
    def reverseBits(self, n: int) -> int:
        
        ## https://www.youtube.com/watch?v=UcoN6UjAI64
        res = 0 ## 32 bit 0
        
        for i in range(32):
            bit = n >> i & 1 ## 32 bit 00..01
            
            res = res | bit << (31 - i)
            
        return res
