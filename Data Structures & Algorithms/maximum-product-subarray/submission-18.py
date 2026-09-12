class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l = 0
        num_neg = 0
        last_neg, second_l_neg = -1, -1
        prod_with_last = -1
        prod_before_second = -1
        max_seen = -1*float('inf')
        
        curr_seen = 1
        for r in range(len(nums)):
            if nums[r] == 0:
                l = r+1
                curr_seen = 1
                max_seen = max(max_seen, 0)
                continue
            # print(curr_seen, nums[r], r)
            max_seen = max(max_seen, curr_seen * nums[r])
            curr_seen *= nums[r]
            if nums[r] < 0:
                num_neg += 1
                if num_neg == 1:
                    last_neg = r
                    prod_with_last = curr_seen
                    # print("L", prod_with_last)
                    continue
                # elif num_neg == 2:
                #     second_l_neg =r
                #     prod_before_second = curr_seen / nums[r]
                #     prod_before_second = prod_before_second / prod_with_last
                # else:
                    # print("L", prod_with_last)
                    # max_seen = max(max_seen, curr_seen/prod_before_second)
            
            max_seen = max(max_seen, curr_seen//prod_with_last)
        return max_seen