class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        seen = set(nums)

        res = 0
        for num in nums:
            if num - 1 in seen:
                continue
            
            seq = 1
            val = num
            while val + 1 in seen:
                seq += 1
                val += 1
            res = max(res, seq)
        return res




