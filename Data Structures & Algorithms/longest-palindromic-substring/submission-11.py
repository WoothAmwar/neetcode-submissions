class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        start, best_len = 0, 1  # any single character is a palindrome

        for i in range(1, n):
            # Two candidate centers per index:
            #   odd  length: center at i       -> (i-1, i+1)   e.g. "ala"
            #   even length: center between    -> (i-1, i)     e.g. "lL"
            for l, r in ((i - 1, i + 1), (i - 1, i)):
                while l >= 0 and r < n and s[l] == s[r]:
                    l -= 1
                    r += 1
                length = r - l - 1  # palindrome spans s[l+1 : r]
                if length > best_len:
                    start, best_len = l + 1, length

        return s[start:start + best_len]