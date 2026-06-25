class Solution:
    def isValid(self, s: str) -> bool:
        my_s = []
        combos = {"]":"[",'}':'{', ')':'('}
        for st in s:
            if st in combos:
                if len(my_s) < 1:
                    return False
                if my_s[-1] == combos[st]:
                    my_s.pop()
                else:
                    return False
            else:
                my_s.append(st)
        print(my_s)
        return len(my_s) == 0