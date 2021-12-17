# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def rec(self, root: 'Node'):
        if not root:
            return
        self.results.append(root.val)
        for child in root.children:
            self.rec(child)

    def preorder(self, root: 'Node') -> List[int]:
        self.results = []
        self.rec(root)
        return self.results


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = [1,None,3,2,4,None,5,6]
    solution=Solution()
    print(solution.rec(root))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
