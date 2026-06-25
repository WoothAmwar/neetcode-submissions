class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenNums = {}

        for idx, n in enumerate(nums):
            wanted_diff = target - n
            if wanted_diff in seenNums:
                return [seenNums[wanted_diff], idx]
            seenNums[n] = idx