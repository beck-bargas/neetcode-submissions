class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i in range(len(nums)):
            hash_map[nums[i]] = i
        
        for i in range(len(nums)):
            res = target - nums[i]
            if res in hash_map and hash_map[res] != i:
                return [i, hash_map[res]]
        