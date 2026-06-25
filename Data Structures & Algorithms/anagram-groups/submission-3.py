class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dct = {}
        for st in strs:
            s_arr = [0]*26
            for ch in st:
                s_arr[ord(ch)-97]+=1

            if tuple(s_arr) in anagram_dct:
                anagram_dct[tuple(s_arr)].append(st)
            else:
                anagram_dct[tuple(s_arr)] = [st]
        return list(anagram_dct.values())