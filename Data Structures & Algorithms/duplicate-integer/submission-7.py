class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        item_dct = {}
        for num in nums:
            if num in item_dct:
                return True
            item_dct[num]=""
        return False