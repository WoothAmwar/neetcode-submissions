class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        # i = 0
        while l <= r: # and i < 5:
            # i+=1
            comp = l + ((r-l) // 2)
            # print(l, r, comp)
            if nums[comp] > target:
                r = comp - 1
            elif nums[comp] < target:
                l = comp + 1
            else:
                # l = comp
                return comp
                
        # print(l, r)
        return -1