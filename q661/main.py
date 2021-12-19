# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        m = len(M)
        if m < 1:
            return M
        n = len(M[0])
        s = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                c = 1
                v = M[i][j]
                for k in [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]:
                    x = i + k[0]
                    y = j + k[1]
                    if x < 0 or x >= m:
                        continue
                    if y < 0 or y >= n:
                        continue
                    c += 1
                    v += M[x][y]
                s[i][j] = v // c
        return s

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    img = [[1,1,1],[1,0,1],[1,1,1]]
    solution=Solution()
    print(solution.imageSmoother(img))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
