class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths are different, they can't be anagrams
        if len(s) != len(t):
            return False
        
        # Array to store frequencies of 26 lowercase characters
        count = [0] * 26
        
        # Count frequencies for both strings simultaneously
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
            
        # If all counts are zero, they are anagrams
        for c in count:
            if c != 0:
                return False
                
        return True