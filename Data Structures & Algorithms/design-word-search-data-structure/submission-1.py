class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        
        def dfs(j: int, node: TrieNode) -> bool:
            curr = node
            for i in range(j, len(word)):
                char = word[i]
                
                if char == '.':
                    # Check all possible paths for the wildcard character
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
                    
            return curr.is_end_of_word

        return dfs(0, self.root)