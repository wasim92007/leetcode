class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = len(strs)
        
        ## If there is one string
        if l == 1:
            return strs[0]
        
        ## Get the length of the first word in the list
        ## We will use this length to check maximum prefix
        lw0 = len(strs[0])
        
        ## Set maximum prefix to an empty string
        max_prefix = ''
        
        ## We will iterate through all the characters in the
        ## word0
        for i in range(lw0):
            ##  Check if the corresponding character is
            ## same for rest of the words
            for word in strs[1:]:
                ## We will handle the scenario when the next
                ## word has length less that word0 with
                ## first condition before the or
                ## We will also stop and return the value if
                ## the character mismatches
                if i == len(word) or strs[0][i] != word[i]:
                    return max_prefix
            ## Increment the max_prefix if for all the words
            ## the corresponding character matches (If condition
            ## above is not executed)
            max_prefix += strs[0][i]
        
        return max_prefix
