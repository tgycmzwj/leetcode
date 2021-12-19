# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]]<temperatures[i]:
                cur_ele=stack.pop()
                res[cur_ele]=i-cur_ele
            stack.append(i)
        return res



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    temperatures = [73,74,75,71,69,72,76,73]
    solution=Solution()
    print(solution.dailyTemperatures(temperatures))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
