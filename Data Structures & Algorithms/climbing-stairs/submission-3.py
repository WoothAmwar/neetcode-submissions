class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0 for _ in range(max(3,n+1))]
        memo[0] = 0
        memo[1] = 1
        memo[2] = 2
        for idx in range(3,n+1):
            memo[idx] = memo[idx-1] + memo[idx-2]
        return memo[n]