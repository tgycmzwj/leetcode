# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = set()
        two_color = [set(), set()]
        for i in range(len(graph)):
            if i not in visited:
                queue = [(i, 0)]
                while queue:
                    node, level = queue.pop()
                    visited.add(node)
                    two_color[level].add(node)
                    for neighbor in graph[node]:
                        if neighbor in two_color[level]:
                            return False
                        if neighbor not in visited:
                            queue.append((neighbor, 1-level))
        return True
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
    graph = [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
    solution=Solution()
    print(solution.isBipartite(graph))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
