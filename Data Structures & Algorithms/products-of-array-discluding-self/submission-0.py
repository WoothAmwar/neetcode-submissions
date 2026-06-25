class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        total_count=0
        real_prod = 1
        for num in nums:
            total_count += 1
            if num==0:
                zero_count+=1
                continue
            real_prod *= num
        output_lst = [0]*total_count
        if zero_count > 1:
            return output_lst
        
        for idx, num in enumerate(nums):
            if zero_count > 0:
                if num != 0:
                    output_lst[idx]=0
                else:
                    output_lst[idx]=real_prod
            else:
                output_lst[idx] = int(real_prod / num)
        return output_lst
        