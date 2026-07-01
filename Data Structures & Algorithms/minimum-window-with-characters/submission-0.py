class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        # Dictionary to keep a count of all the unique characters in t.
        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
            
        window = {}
        have, need = 0, len(countT)
        
        # res stores: [length_of_window, left_index, right_index]
        res, res_len = [-1, -1], float("inf")
        l = 0
        
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            
            # If the current character's frequency matches the requirement in t
            if c in countT and window[c] == countT[c]:
                have += 1
                
            # Try to shrink the window from the left while it remains valid
            while have == need:
                # Update our result if this window is smaller than the minimum found so far
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                    
                # Pop the leftmost character out of the window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
                
        l, r = res
        return s[l : r + 1] if res_len != float("inf") else ""