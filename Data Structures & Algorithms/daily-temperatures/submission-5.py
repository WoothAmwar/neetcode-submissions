class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempStack = [] # (temp, num it popped off)
        output = []
        popped = 0
        passed = 0
        # p = 0
        for idx, curr_t in enumerate(temperatures[::-1]):
            if len(tempStack) == 0:
                tempStack.append((curr_t,0))
                output = [0]
                print(-1, curr_t, output, tempStack)
                continue
            while len(tempStack) != 0: # and p<15:
                # p += 1
                # print(output)
                if curr_t < tempStack[-1][0]:
                    tempStack.append((curr_t, passed))

                    # Adding to start of list
                    output.append(passed+1)

                    passed = 0
                    popped = 0
                    print(1, curr_t,output, tempStack)
                    break
                else:
                    passed += 1 + tempStack[-1][1]
                    tempStack.pop()
                    print(2, curr_t,output, tempStack)

                if len(tempStack) == 0:
                    output.append(0)
                    tempStack.append((curr_t, 0))
                    passed = 0
                    popped = 0
                    print(0, curr_t, output, tempStack)
                    break


        print(tempStack)
        return output[::-1]