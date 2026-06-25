class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Find row
        rl, rr = 0, len(matrix)-1
        t_row = -1
        i = 0

        while rl <= rr and i < 5:
            i += 1
            comp_r = rl + (rr-rl)//2
            did = False
            print(rl, rr, comp_r)
            if target <= matrix[comp_r][-1]:
                rr = comp_r-1
                did=True
            
            if matrix[comp_r][0] <= target:
                rl = comp_r+1
                did=True
            if not did:
                break
            
        print(t_row, "O:", comp_r, ":", matrix[comp_r])
        # if t_row == -1:
        #     return False
        comp_row = matrix[comp_r]

        ml, mr = 0, len(comp_row) - 1
        while ml <= mr:
            comp_m = ml + (mr - ml)//2
            if comp_row[comp_m] < target:
                ml = comp_m + 1
            elif comp_row[comp_m] > target:
                mr = comp_m - 1
            else:
                return True
        return False
