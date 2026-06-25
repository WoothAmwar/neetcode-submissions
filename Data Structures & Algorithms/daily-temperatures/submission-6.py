class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempStack = [] # (temp, num it popped off)
        output = []
        passed = 0
        for idx, curr_t in enumerate(temperatures[::-1]):
            if len(tempStack) == 0:
                tempStack.append((curr_t,0))
                output = [0]
                continue
            while len(tempStack) != 0:
                if curr_t < tempStack[-1][0]:
                    tempStack.append((curr_t, passed))

                    output.append(passed+1)

                    passed = 0
                    break
                else:
                    passed += 1 + tempStack[-1][1]
                    tempStack.pop()

                if len(tempStack) == 0:
                    output.append(0)
                    tempStack.append((curr_t, 0))
                    passed = 0
                    popped = 0
                    break
        return output[::-1]