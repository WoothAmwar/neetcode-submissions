class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        s_nums = nums
        freq = {}
        for n in s_nums:
            freq[n] = freq.get(n, 0)+1
        freq_v = sorted(freq.items(), key=lambda item: item[1]) 
        final = []
        for i in range(k):
            idx = len(freq_v)-i-1
            final.append(freq_v[idx][0])
        return final