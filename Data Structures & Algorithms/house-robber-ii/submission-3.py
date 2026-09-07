class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        start_dp = [-1] * (len(nums) - 1)
        start_dp[0] = nums[0]
        start_dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums) - 1):
            start_dp[i] = max(start_dp[i - 1], start_dp[i - 2] + nums[i])
        
        end_dp = [-1] * (len(nums) - 1)
        end_dp[0] = nums[1]
        end_dp[1] = max(nums[1], nums[2])

        for i in range(2, len(nums) - 1):
            end_dp[i] = max(end_dp[i - 1], end_dp[i - 2] + nums[i + 1])
        
        return max(start_dp[-1], end_dp[-1])