class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        max_length = 0
        
        for r in range(len(s)):
            # If a duplicate is found, shrink the window from the left
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
                
            # Add the current character to the window
            char_set.add(s[r])
            
            # Update the max length found so far
            max_length = max(max_length, r - l + 1)
            
        return max_length