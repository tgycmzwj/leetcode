# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
from collections import deque
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if not maze or not start or not destination:
            return False
        if start == destination:
            return True
        q = deque([(start[0], start[1])])
        visited = set()
        directions_to_go = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            current = q.popleft()
            if current[0] == destination[0] and current[1] == destination[1]:
                return True
            for direction in directions_to_go:
                x = current[0] + direction[0]
                y = current[1] + direction[1]
                while 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0:
                    x += direction[0]
                    y += direction[1]
                rolled_to_x = x - direction[0]
                rolled_to_y = y - direction[1]
                if (rolled_to_x, rolled_to_y) not in visited:
                    visited.add((rolled_to_x, rolled_to_y))
                    q.append((rolled_to_x, rolled_to_y))
        return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
    start = [0,4]
    destination = [4,4]
    solution=Solution()
    print(solution.hasPath(maze,start,destination))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
