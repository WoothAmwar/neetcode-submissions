class Solution:
    def longestPalindrome(self, s: str) -> str:
        # abbcdfdcb
        sl = list(s)
        if len(sl) == 1:
            return s
        if len(sl) == 2:
            if sl[0] == sl[1]:
                return s
            else:
                return sl[0]

        longest_substring = (0, 0)
        ls = 0
        long_len = 0
        sl.append("$")
        for l_idx, l in enumerate(sl[0:-1]):
            if l_idx == 0 or l_idx == len(sl):
                continue
            if l == sl[l_idx-1] or sl[l_idx-1] == sl[l_idx+1]:
                if sl[l_idx-1] == sl[l_idx+1]:
                    # l = middle of ala
                    ll, rl = l_idx, l_idx

                    while sl[ll] == sl[rl]:
                        if ls <= rl-ll:
                            longest_substring = (ll, min(rl+1, len(sl)))
                            ls = max(ls, longest_substring[1] - longest_substring[0])
                        ll-=1
                        rl+=1
                        if ll < 0 or rl > len(sl):
                            break
                if l == sl[l_idx-1]:
                    # L = end of lL
                    ll, rl = l_idx-1, l_idx
                    while sl[ll] == sl[rl]:
                        if ls <= rl-ll:
                            longest_substring = (ll, min(rl+1, len(sl)))
                            ls = max(ls, longest_substring[1] - longest_substring[0])
                        ll-=1
                        rl+=1
                        if ll < 0 or rl > len(sl):
                            break
        return ''.join(sl[longest_substring[0]:longest_substring[1]])