class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # print("L", k)
        freq_table = {}
        freq_counter = [[] for _ in range(len(nums))]
        # print("BEFL", freq_counter)
        for num in nums:
            if num in freq_table:
                freq_table[num] += 1
            else:
                freq_table[num] = 1
            freq_counter[freq_table[num] -1].append(num)
            # print(freq_counter)
        # print(freq_table)
        # print("DSFKJ")
        # print(freq_counter)
        ans = set()
        for i in range(0, len(nums)):
            for j in freq_counter[len(nums)-i-1]:
                ans.add(j)
            # print(len(ans), k, len(ans)==k, ans)
            if len(ans) == k:
                print("ANS:", ans)
                return list(ans)
        