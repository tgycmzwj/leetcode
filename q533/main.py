# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
from collections import defaultdict
class Solution:
    def findBlackPixel(self, picture: List[List[str]], target: int) -> int:
        m, n = len(picture), len(picture[0])
        freq = defaultdict(int)
        rows = [0] * m
        cols = [0] * n
        for i in range(m):
            for j in range(n):
                if picture[i][j] == "B":
                    rows[i] += 1
                    cols[j] += 1
            freq["".join(picture[i])] += 1

        ans = 0
        for i in range(m):
            key = "".join(picture[i])
            if freq[key] == target:
                for j in range(n):
                    if picture[i][j] == "B" and rows[i] == cols[j] == target: ans += 1
        return ans

    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    picture = [["W","B","W","B","B","W"],["W","B","W","B","B","W"],["W","B","W","B","B","W"],["W","W","B","W","B","W"]]
    target = 3
    solution=Solution()
    print(solution.findBlackPixel(picture,target))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
