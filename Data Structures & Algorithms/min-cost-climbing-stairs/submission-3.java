class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int[] step_c = new int[cost.length + 1];
        step_c[0] = cost[0];
        step_c[1] = cost[1];
        for (int i=2; i<cost.length; i++) {
            step_c[i] = Math.min(step_c[i-1], step_c[i-2]) + cost[i];
        }
        return Math.min(step_c[cost.length-1], step_c[cost.length-2]);
    }
}
