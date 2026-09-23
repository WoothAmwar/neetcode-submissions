class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sols = [[]]
        true_sols = []

        for n in nums:
            for subset in sols:
                if sum(subset+[n]) > target:
                    continue
                sols += [subset + [n]]
        for s in sols:
            if sum(s) == target:
                true_sols.append(s)
        return true_sols