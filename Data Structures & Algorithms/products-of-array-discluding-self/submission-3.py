class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sum_x_0 = 0
        zero_in = 0
        for n in nums:
            if n != 0:
                if sum_x_0 == 0:
                    sum_x_0 = 1
                sum_x_0 *= n
            else:
                zero_in += 1

        output = []
        for n in nums:
            if n != 0:
                if zero_in > 0:
                    output.append(0)
                else:
                    if zero_in > 1:
                        output.append(0)
                    else:   
                        output.append(int(sum_x_0/n))
            else:
                if zero_in > 1:
                    output.append(0)
                else:
                    output.append(sum_x_0)
        return output