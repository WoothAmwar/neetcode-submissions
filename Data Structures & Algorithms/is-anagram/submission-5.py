class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_1 = {}
        for c in s:
            if c in char_1:
                char_1[c] = char_1[c]+1
            else:
                char_1[c] = 1
        
        for c in t:
            if c in char_1:
                char_1[c] -= 1
                if (char_1[c] < 0):
                    return False
            else:
                return False
        
        return sum(char_1.values())==0
            
