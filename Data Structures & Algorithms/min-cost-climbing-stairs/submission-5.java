class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int l = cost.length;
        int[] step_c = new int[l + 1];
        step_c[0] = cost[0];
        step_c[1] = cost[1];
        for (int i=2; i<l; i++) {
            step_c[i] = Math.min(step_c[i-1], step_c[i-2]) + cost[i];
        }
        return Math.min(step_c[l-1], step_c[l-2]);
    }
}
