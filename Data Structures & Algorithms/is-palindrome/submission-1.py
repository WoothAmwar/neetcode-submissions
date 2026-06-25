class Solution:
    def isPalindrome(self, s: str) -> bool:
        start_idx = 0
        end_idx = len(s)-1
        while start_idx <= end_idx:
            if not s[start_idx].isalnum():
                start_idx += 1
                continue
            if not s[end_idx].isalnum():
                end_idx -= 1
                continue
            
            if s[start_idx].lower() == s[end_idx].lower():
                start_idx += 1
                end_idx -= 1
            else:
                return False
            
        return True
