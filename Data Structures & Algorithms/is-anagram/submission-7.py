class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dct = {}
        # t_dct = {}
        for s_let in s:
            s_dct[s_let] = s_dct.get(s_let, 0)+1
        for t_let in t:
            s_dct[t_let] = s_dct.get(t_let, 0)-1
            if s_dct[t_let]<0:
                return False
        return sum(s_dct.values())==0
        
