class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out_arr = []
        max_arr = []
        for idx, curr_t in enumerate(temperatures[::-1]):
            if not max_arr:
                out_arr.append(0)
                max_arr.append((curr_t, idx))
                continue
            while curr_t >= max_arr[-1][0]:
                max_arr.pop(-1)
                if not max_arr:
                    # out_arr.append(0)
                    max_arr.append((curr_t, idx))
                    break
            print(curr_t, "ID", max_arr)
            out_arr.append(idx - max_arr[-1][1])
            max_arr.append((curr_t, idx))
        return out_arr[::-1]

            