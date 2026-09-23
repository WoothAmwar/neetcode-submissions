class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sols = [[]]
        # forms = []

        for n in nums:
            sols += [subset + [n] for subset in sols]
        # print("FI", sols)
        return sols