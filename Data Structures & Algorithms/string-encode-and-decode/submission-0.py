class Solution:
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            # Format: <length>#<string>
            res.append(str(len(s)) + "#" + s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            # Find the delimiter tracking the end of the length prefix
            while s[j] != '#':
                j += 1
                
            # Extract the length of the upcoming string
            length = int(s[i:j])
            
            # The string starts right after the '#' character
            start_of_str = j + 1
            end_of_str = start_of_str + length
            
            res.append(s[start_of_str:end_of_str])
            
            # Move pointer to the start of the next encoded block
            i = end_of_str
            
        return res