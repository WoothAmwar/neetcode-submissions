class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        used_starts = set()

        for idx, num in enumerate(nums):
            if num > 0:
                break
            if num in used_starts:
                continue
            used_starts.add(num)
            sum_to = 0 - num

            l=idx+1
            r = len(nums)-1
            used_pairs = set()
            while l<r:
                if l == idx:
                    l+=1
                if r == idx:
                    r+=1
                if l > len(nums)-1 or r < 0:
                    break
                two_sum = nums[l] + nums[r]
                if two_sum == sum_to:
                    if (nums[l], nums[r]) not in used_pairs:
                        print(idx)
                        output.append([nums[l], nums[r], num])
                        used_pairs.add((nums[l], nums[r]))
                
                if two_sum > sum_to:
                    r-=1
                else:
                    l+=1
        return output