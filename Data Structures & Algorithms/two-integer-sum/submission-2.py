class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_nums = {}
        for idx, num in enumerate(nums):
            if num in seen_nums:
                return [seen_nums[num], idx]
            seen_nums[target-num]=idx