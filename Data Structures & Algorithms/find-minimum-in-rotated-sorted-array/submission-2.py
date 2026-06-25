class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        # i = 0
        if nums[l] < nums[r]:
            return nums[l]
        while r - l > 1: # and i < 10:
            # i+=1
            m = (r + l) // 2
            print(l, r, m, nums[m])
            if nums[m] > nums[l]:
                l = m
            elif nums[m] < nums[r]:
                r = m
        # print(l, r, m)
        return min(nums[l], nums[r])
