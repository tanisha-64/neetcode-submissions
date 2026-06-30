class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_length = 0
        max_freq = 0
        l = 0
        
        for r in range(len(s)):
            # Update frequency of the current character
            count[s[r]] = 1 + count.get(s[r], 0)
            # Track the maximum frequency of a single character in the current window
            max_freq = max(max_freq, count[s[r]])
            
            # If the number of remaining characters to replace exceeds k, shrink window
            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1
                
            # Update the absolute maximum length found
            max_length = max(max_length, r - l + 1)
            
        return max_length