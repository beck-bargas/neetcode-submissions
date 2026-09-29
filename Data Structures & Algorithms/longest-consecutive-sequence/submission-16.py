class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: 
        nums = set(nums)
        
        res = 0
        for num in nums:
            if num - 1 not in nums:
                val = num
                cons = 1

                while val + 1 in nums:
                    val += 1
                    cons += 1
                res = max(res, cons)
        return res