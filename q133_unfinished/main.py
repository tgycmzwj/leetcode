# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def build_graph(adjList:List[List[int]])->'Node':


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    adjList = build_graph([[2,4],[1,3],[2,4],[1,3]])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
