class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_s = ""
        alpha_len = 0
        for char in s:
            if char.isalnum():
                alpha_s += char.lower()
                alpha_len += 1
        for st_idx in range(int(alpha_len/2)):
            if alpha_s[st_idx] != alpha_s[-1 * (st_idx+1)]:
                return False
        return True