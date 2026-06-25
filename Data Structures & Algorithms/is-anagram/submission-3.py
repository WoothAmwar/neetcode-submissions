class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c_hash = {}
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for c in alphabet:
            c_hash[c] = 0
        
        for ch in s:
            c_hash[ch] = c_hash[ch] + 1
        
        for ch in t:
            if c_hash[ch] == 0:
                return False
            c_hash[ch] = c_hash[ch]-1
        
        if sum(list(c_hash.values())) == 0:
            return True
        return False
            
