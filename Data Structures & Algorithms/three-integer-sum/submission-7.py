class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res = []
        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                l = j + 1
                r = len(nums) - 1
                target = -(nums[i] + nums[j])
                
                while l <= r:
                    mid = (l + r) // 2

                    if nums[mid] < target:
                        l = mid + 1
                    elif nums[mid] > target:
                        r = mid - 1
                    else:
                        res.append([nums[i], nums[j], nums[mid]])
                        break
        return res
                