class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sols = [[]]
        true_sols = []

        for n in nums:
            for subset in sols:
                s = sum(subset+[n])
                if s > target:
                    continue
                elif s == target:
                    true_sols.append(subset+[n])
                sols += [subset + [n]]
        return true_sols