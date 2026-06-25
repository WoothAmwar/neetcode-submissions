class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ""
        for s in strs:
            l = len(s)
            final += str(l) + "#"
            final += s
        print("F:", final)
        return final

    def decode(self, s: str) -> List[str]:
        s_c = s
        output = []
        while s_c:
            ds_o = s_c.split("#")[0]
            go_forward = int(ds_o)
            if go_forward == 0:
                output.append("")
                print("S:", s_c)
                s_c = s_c[2:]
                continue
            s_c = s_c[len(ds_o)+1:]
            print(go_forward, s_c[0:go_forward])
            output.append(s_c[0:go_forward])
            s_c = s_c[go_forward:]
        return output
