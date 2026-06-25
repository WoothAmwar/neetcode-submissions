class Solution:
    def isValid(self, s: str) -> bool:
        # pairs = {'[':']', '{':'}', '(':')'}
        closing = {']':'[', '}':'{', ')':'('}
        curr_lst = []
        for ch in s:
            if curr_lst and ch in closing and curr_lst[-1] == closing[ch]:
                curr_lst.pop()
            else:
                curr_lst.append(ch)
        return len(curr_lst)==0

        