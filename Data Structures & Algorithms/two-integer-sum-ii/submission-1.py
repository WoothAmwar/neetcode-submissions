class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        compliment_dct = defaultdict(int)
        for idx, num in enumerate(numbers):
            if num not in compliment_dct:
                compliment_dct[target-num] = idx
            else:
                return [idx+1, compliment_dct[num]+1] if idx<compliment_dct[num] else [compliment_dct[num]+1, idx+1]