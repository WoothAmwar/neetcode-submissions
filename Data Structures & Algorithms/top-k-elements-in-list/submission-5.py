class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_table = {}
        freq_counter = [[] for _ in range(len(nums))]
        for num in nums:
            if num in freq_table:
                freq_table[num] += 1
            else:
                freq_table[num] = 1
            freq_counter[freq_table[num] -1].append(num)
        ans = set()
        for i in range(len(nums)-1, -1, -1):
            for j in freq_counter[i]:
                ans.add(j)
            if len(ans) == k:
                print("ANS:", ans)
                return list(ans)
        # list(range(len(nums)-1, -1, -1))