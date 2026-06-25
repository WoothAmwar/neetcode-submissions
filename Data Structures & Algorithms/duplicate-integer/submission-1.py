class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lst = []
        for i in nums:
            if i in lst:
                return True
            lst.append(i)
        return False