from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Map character count tuple to list of anagrams
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Create a frequency array for 'a' through 'z'
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            # Convert list to tuple to make it a valid dictionary key
            anagram_map[tuple(count)].append(s)
            
        return list(anagram_map.values())