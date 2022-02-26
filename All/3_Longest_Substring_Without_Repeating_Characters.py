class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        ## Algorithm:
        ## Leetcode: https://www.youtube.com/watch?v=wiGpQwVHdE0
        ## We will have a sliding two pointer approch. We will
        ## keep on incrementing the right pointer till we hit 
        ## the end. We will increment left pointer till we have
        ## only unique characters.

        ans, lp = 0, 0
        char_set = set()

        ## We will keep incrementing the right pointer rp using
        ## this for loop
        for rp in range(len(s)):
            ## If the new incremented char is in char set, we
            ## will keep on removing element from the left till
            ## we have only unique character.
            while s[rp] in char_set:
                ## Remove character
                char_set.remove(s[lp])
                ## Increment the left pointer lp
                lp += 1

            ## Add the new charater to the set
            char_set.add(s[rp])
            ## Update our answer
            ans = max(ans, rp-lp+1) ## +1 when rp=lp

        return ans
