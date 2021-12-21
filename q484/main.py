# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List


class Solution:
    def findPermutation(self, s: str) -> List[int]:
        stack = []
        prev = 0
        ans = [0] * (len(s) + 1)
        for i, ch in enumerate(s + "I"):
            if (ch == "I"):
                prev = prev + 1
                ans[i] = prev
                while (stack):
                    prev += 1
                    ans[stack.pop()] = prev
            else:
                stack.append(i)
        return ans




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s="DDDDIDIIIDID"
    solution=Solution()
    print(solution.findPermutation(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
