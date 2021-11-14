class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        r = 0
        for c in columnTitle:
            r = r*26 + ord(c) - 64
            
        return r
