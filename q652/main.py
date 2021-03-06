# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import Optional
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def build_tree(s):
    if len(s)==0:
        return
    root=TreeNode(s[0])
    s.pop(0)
    ongoing_list=[root]
    while len(ongoing_list)!=0:
        cur_node=ongoing_list.pop(0)
        while cur_node.val==None:
             cur_node=ongoing_list.pop(0)
        if len(s)!=0:
            left_node=TreeNode(s.pop(0))
        else:
            break
        if left_node.val!=None:
            cur_node.left = left_node
            ongoing_list.append(left_node)
        if len(s)!=0:
            right_node=TreeNode(s.pop(0))
        else:
            break
        if right_node.val!=None:
            cur_node.right=right_node
            ongoing_list.append(right_node)
    return root

from collections import defaultdict
class Solution:
    def preorder(self,node):
        if node is None:
            return '#'
        L = self.preorder(node.left)
        R = self.preorder(node.right)
        this = ','.join((str(node.val), L, R))
        self.serialisationCount[this] += 1
        self.serialisationNode[this] = node
        return this
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # preorder traversal serialisation map to node + count
        self.serialisationCount = defaultdict(int)
        self.serialisationNode = {}
        self.preorder(root)
        return [self.serialisationNode[serialisation] for serialisation in self.serialisationCount if
                self.serialisationCount[serialisation] >= 2]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = [1,2,3,4,None,2,4,None,None,4]
    root=build_tree(root)
    solution=Solution()
    print(solution.findDuplicateSubtrees(root))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
