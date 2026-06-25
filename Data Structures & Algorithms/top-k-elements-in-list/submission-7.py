class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dct = defaultdict(int)
        count = 0
        for num in nums:
            freq_dct[num] = freq_dct[num]+1
            count += 1
        counter_arr = [[] for _ in range(count+1)]
        for num in freq_dct:
            counter_arr[freq_dct[num]].append(num)
        
        result = []
        total = 0
        for idx in range(count,0, -1):
            if len(counter_arr[idx]) != 0:
                for res in counter_arr[idx]:
                    result.append(res)
                    total += 1
            if total >= k:
                return result