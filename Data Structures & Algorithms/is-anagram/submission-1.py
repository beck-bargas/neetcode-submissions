class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def hash_word(word):
            hash = defaultdict(int)
            for c in word:
                hash[c] += 1
            return hash
        return hash_word(s) == hash_word(t)
