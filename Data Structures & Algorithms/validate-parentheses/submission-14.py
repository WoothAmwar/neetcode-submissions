class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'[':']', '{':'}', '(':')'}
        closing = {']':'[', '}':'{', ')':'('}
        curr_lst = []
        for ch in s:
            if ch not in pairs:
                if ch not in closing or len(curr_lst)<1:
                    return False
                if curr_lst[-1] == closing[ch]:
                    curr_lst.pop()
                else:
                    return False
            if ch in pairs:
                curr_lst.append(ch)
        return len(curr_lst)==0

        