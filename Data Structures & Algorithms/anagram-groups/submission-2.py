class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_output = []
        output_format = {}  # set, lst
        for s in strs:
            s_set = [0]*26
            for l in s:
                s_set[ord(l)-ord('a')] += 1
            if tuple(s_set) in output_format:
                output_format[tuple(s_set)].append(s)
            else:
                output_format[tuple(s_set)] = [s]
        return output_format.values()