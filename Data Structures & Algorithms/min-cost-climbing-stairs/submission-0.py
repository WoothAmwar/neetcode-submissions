class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost_tracker = [0 for _ in range(len(cost)+1)]
        cost.append(0)

        for st_idx, st_cost in enumerate(cost):
            if st_idx <= 1:
                continue
            cost_tracker[st_idx] = min(cost_tracker[st_idx-2]+cost[st_idx-2], cost_tracker[st_idx-1]+cost[st_idx-1]) 
        #     print(st_idx, st_cost, cost_tracker[st_idx-2]+cost[st_idx-2], cost_tracker[st_idx-1]+cost[st_idx-1])
        # print(cost_tracker)
        return cost_tracker[-1]