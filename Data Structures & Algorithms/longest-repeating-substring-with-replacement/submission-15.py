class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0

        characters = set(list(s))

        max_size = 0

        for ch in characters:
            l, r = -1, -1  # l is exclusive, r are inclusize
            # l is the first character which isn't included
            #. r is the last character which is included
            left = k
            last_ch = -1

            for idx, st in enumerate(list(s)):
                if st == ch:
                    r += 1
                else:
                    left -= 1
                    if left < 0:
                        l += 1
                        while list(s)[l] == ch:
                            l += 1
                        left = 0
                    r += 1
                
                r = max(r, l)

                max_size = max(r-l, max_size)
        return max_size
