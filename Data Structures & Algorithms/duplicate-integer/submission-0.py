class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_nums = set()
        for n in nums:
            if n in seen_nums:
                return True
            seen_nums.add(n)
        return False