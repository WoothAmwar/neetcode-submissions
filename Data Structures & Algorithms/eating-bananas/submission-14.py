class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # case where h = len(piles), eat each pile in 1 hour
        if h == len(piles):
            return max(piles)

        span = (1, max(piles))
        works = span[1]
        passes = False
        t_h = 0
        while True:
            t_h = 0
            initial = (span[0] + span[1]) // 2
            passes = False
            for p in piles:
                t_h += math.ceil(p/initial)
            if t_h <= h:
                passes = True
            # print(initial, works, span)
            if not passes:
                span = (initial+1, span[1])
            else:
                span = (span[0], initial)
                works = initial

            if span[1] - span[0] < 1:
                return works


        