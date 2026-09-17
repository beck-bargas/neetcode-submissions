class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            buckets = [0] * 26
            for c in s:
                idx = ord(c) - ord('a')
                buckets[idx] += 1
            anagrams[tuple(buckets)].append(s)
        
        res = []
        for s in anagrams.values():
            res.append(s)
        return res

        