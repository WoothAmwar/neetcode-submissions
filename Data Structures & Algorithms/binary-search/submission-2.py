class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start_idx = 0
        end_idx = len(nums)-1
        comp_idx = (start_idx + end_idx) // 2
        while nums[comp_idx] != target:
            comp_idx = (start_idx + end_idx) // 2
            print(start_idx, end_idx, comp_idx)
            if target > nums[comp_idx]:
                start_idx = comp_idx
            elif target < nums[comp_idx]:
                end_idx = comp_idx
            else:
                return comp_idx
            
            if abs(start_idx - end_idx) <= 1:
                if nums[start_idx] == target:
                    return start_idx
                if nums[end_idx] == target:
                    return end_idx
                return -1
            
        return comp_idx
        