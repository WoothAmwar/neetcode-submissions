class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dct = {}
        t_dct = {}
        for s_let in s:
            s_dct[s_let] = s_dct.get(s_let, 0)+1
        for t_let in t:
            t_dct[t_let] = t_dct.get(t_let, 0)+1
        return s_dct == t_dct
        
