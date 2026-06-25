class Solution:
    def maxArea(self, heights: List[int]) -> int:
        out_max = 0
        l, r = 0, len(heights)-1
        while l < r:
            base_len = r-l
            height = min(heights[l],heights[r])
            out_max = max(out_max, height*base_len)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return out_max