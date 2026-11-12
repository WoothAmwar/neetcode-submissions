class Solution {
    public int climbStairs(int n) {
        ArrayList<Integer> step_c = new ArrayList<>();
        step_c.add(1);
        step_c.add(2);
        for (int i=2; i<n; i++) {
            step_c.add(step_c.get(i-1) + step_c.get(i-2));
        }

        return step_c.get(n-1);
    }
}
