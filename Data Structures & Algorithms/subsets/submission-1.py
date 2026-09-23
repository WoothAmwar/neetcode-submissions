class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sols = [[]]

        for n in nums:
            sols += [subset + [n] for subset in sols]
        return sols