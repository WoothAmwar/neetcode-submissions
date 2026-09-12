class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return nums[0]
        l = 0
        num_neg = 0
        prod_with_last = 1
        max_seen = -1*float('inf')
        
        curr_seen = 1
        for r in range(len(nums)):
            if nums[r] == 0:
                l = r+1
                curr_seen = 1
                max_seen = max(max_seen, 0)
                continue
            curr_seen *= nums[r]
            max_seen = max(max_seen, curr_seen, curr_seen//prod_with_last)
            if nums[r] < 0:
                num_neg += 1
                if num_neg == 1:
                    prod_with_last = curr_seen
                    continue
        return max_seen