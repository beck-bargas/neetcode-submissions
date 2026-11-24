class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(i, curr):
            if i >= len(word):
                return curr.word

            if word[i] == ".":
                for child in curr.children.values():
                    if dfs(i + 1, child):
                        return True
            if word[i] not in curr.children:
                return False
            
            curr = curr.children[word[i]]
            return dfs(i + 1, curr)
        return dfs(0, self.root)
