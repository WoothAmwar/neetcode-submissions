import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower_bound = 1
        upper_bound = max(piles)
        res = upper_bound
        
        while lower_bound <= upper_bound:
            k = (lower_bound + upper_bound) // 2
            tot_time = 0
            for pile in piles:
                tot_time += math.ceil(pile / k)
            if tot_time <= h:
                res = k
                upper_bound = k - 1
            elif tot_time > h:
                lower_bound = k+1
        return res
