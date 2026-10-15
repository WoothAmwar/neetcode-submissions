class Solution:
    def rob(self, nums: List[int]) -> int:
        running_sum = [0 for _ in range(len(nums))]
        if len(nums) <= 2:
            return max(nums)
        running_sum[0] = nums[0]
        running_sum[1] = max(nums[0], nums[1])
        for h_idx, h_val in enumerate(nums):
            if h_idx < 2:
                continue
            running_sum[h_idx] = max(running_sum[h_idx-2]+h_val, running_sum[h_idx-1])
        return max(running_sum[-1], running_sum[-2])