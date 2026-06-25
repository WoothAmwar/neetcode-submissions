class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return_output = []
        anagram_dict_pairs = defaultdict(list)

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')] += 1
            anagram_dict_pairs[tuple(count)].append(s)
        return anagram_dict_pairs.values()