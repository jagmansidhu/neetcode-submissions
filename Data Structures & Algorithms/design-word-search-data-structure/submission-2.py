class node:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = node()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = node()
            cur = cur.children[c]
        cur.end = True
        return

    def search(self, word: str) -> bool:
        def dfs(index, child): 
            cur = child

            for c in range(index, len(word)):                
                char = word[c]
                if char == ".":
                    for ch in cur.children:
                        if dfs(c + 1, cur.children[ch]):
                            return True
                    return False
                else:
                    if char not in cur.children:
                        return False
                    cur = cur.children[char]

            return cur.end
                    
        return dfs(0, self.root)
        

#  tries dsa with bfs for searching