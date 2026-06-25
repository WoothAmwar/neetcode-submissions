class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        seen_letters = set()
        max_len = 0
        if len(s) <= 1:
            print("DEF")
            return len(s)
        while r < len(s):
            if s[r] in seen_letters:
                print(l, r, max_len, r-l-1)
                max_len = max(max_len, r - l)
                seen_letters.discard(s[r])
                while s[l] != s[r]:
                    seen_letters.discard(s[l])
                    l+=1
                l+=1
            # max_len = max(max_len, r - l)
            seen_letters.add(s[r])
            r += 1
        max_len = max(max_len, r - l)
        return max_len