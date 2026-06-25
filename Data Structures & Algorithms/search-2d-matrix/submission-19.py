class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Find row
        rl, rr = 0, len(matrix)-1

        while rl <= rr:
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

        comp_row = matrix[comp_r]
        # Find in row
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
