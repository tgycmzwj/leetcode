# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import collections
from typing import List
class Solution:
    def bfs(self, src, dst, G):
        if not (src in G and dst in G): return -1.0
        q, seen = [(src, 1.0)], set()
        for x, v in q:
            if x == dst:
                return v
            seen.add(x)
            for y in G[x]:
                if y not in seen:
                    q.append((y, v * G[x][y]))
        return -1.0
    def calcEquation(self, equations, values, queries):
        G = collections.defaultdict(dict)
        for (x, y), v in zip(equations, values):
            G[x][y] = v
            G[y][x] = 1 / v
        return [self.bfs(s, d, G) for s, d in queries]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
    values = [1.5, 2.5, 5.0]
    queries = [["a", "c"], ["c", "b"],["bc", "cd"], ["cd", "bc"]]
    print(solution.calcEquation(equations,values,queries))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
