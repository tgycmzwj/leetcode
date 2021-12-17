# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if len(ops)==0:
            return m*n
        min_m,min_n=min([i[0] for i in ops]),min([i[1] for i in ops])
        return min_m*min_n

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    m = 3
    n = 3
    ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
    solution=Solution()
    print(solution.maxCount(m,n,ops))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
