# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        if len(root.children) == 0:
            return 1
        return max([self.maxDepth(child) for child in root.children]) + 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = [1, Node, 3, 2, 4, Node, 5, 6]
    solution=Solution()
    print(solution.maxDepth(root))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
