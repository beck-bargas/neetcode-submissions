class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: 
        nums = set(nums)
        
        res = 0
        for num in nums:
            val = num

            cons = 1
            while val - 1 in nums and num + 1 not in nums:
                cons += 1
                val -= 1
            res = max(res, cons)
        return res