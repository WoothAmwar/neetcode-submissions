class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sols = [[]]
        true_sols = []

        for n in nums:
            for subset in sols:
                sn = subset+[n]
                s = sum(sn)
                if s > target:
                    continue
                elif s == target:
                    true_sols.append(sn)
                sols += [sn]
        return true_sols