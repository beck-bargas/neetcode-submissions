class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}

        for i, num in enumerate(nums):
            res = target - num
            if res in count:
                return [count[res], i]
            count[num] = i

