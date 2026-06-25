class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needed_dct = {}
        for idx, num in enumerate(nums):
            if target-num in needed_dct:
                return [needed_dct[target-num], idx]
            needed_dct[num] = idx
            print(needed_dct)