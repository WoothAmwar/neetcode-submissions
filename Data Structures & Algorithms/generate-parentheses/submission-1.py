class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Probably solve using recursion, then look at solution
        """
        total_correct = []
        def gen_par(self, max_len, curr_str, curr_open):
            curr_val = 0
            for ch in curr_str:
                if ch == "(":
                    curr_val += 1
                else:
                    curr_val -= 1
            if curr_val < 0:
                return
            if len(curr_str) == max_len:
                if curr_val == 0:
                    total_correct.append(curr_str)
                return
            l = gen_par(self,max_len, curr_str+"(", curr_open+1)
            r = gen_par(self,max_len, curr_str+")", curr_open)

            return l, r
        gen_par(self, n*2, "(", 0)
        return total_correct

                

        
