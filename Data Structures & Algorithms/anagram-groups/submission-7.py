class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dct = {} # key=001... , value=list of strings

        for s in strs:
            s_sp = s
            bit_m = [0 for _ in range(26)]
            for l in s_sp:
                bit_m[ord(l)-ord('a')] += 1
            for l in range(len(bit_m)):
                bit_m[l] = str(bit_m[l])
            s_key = '|'.join(bit_m)
            print(s_key)
            # s_key = ''.join([str(ord('a')-ord(l)) for l in s_sp])
            x = str_dct.get(s_key, [])
            x.append(s)
            str_dct[s_key] = x
        print(str_dct)
        return list(str_dct.values())