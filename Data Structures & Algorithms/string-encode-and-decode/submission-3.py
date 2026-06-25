class Solution:

    def encode(self, strs: List[str]) -> str:
        len_lst = []
        for st in strs:
            len_lst.append(len(st))
        output_str = ""
        for idx, st in enumerate(strs):
            output_str += str(len_lst[idx]) + "_"
            output_str += st
        return output_str

    def decode(self, s: str) -> List[str]:
        output_lst = []
        word_idx = 0
        rest = s
        curr_len = 0
        curr_idx=0
        while curr_idx <= len(s):
            if "_" not in rest:
                return output_lst
            sp = rest[curr_len:].split("_")
            rest = rest[curr_len + len(sp[0])+1 :]

            curr_word = ""
            curr_len = int(sp[0])
            for let_idx in range(curr_len):
                curr_word += rest[let_idx]
            output_lst.append(curr_word)
            # if "_" not in rest:
            #     return output_lst
        return output_lst

        