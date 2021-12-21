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

class TreeNode_cust(TreeNode):
    def __init__(self,root):
        super(TreeNode_cust, self).__init__()
        self.val=root.val
        if root.left:self.left=TreeNode_cust(root.left)
        if root.right:self.right=TreeNode_cust(root.right)
        self.left_depth=0
        self.right_depth=0
        self.left_values=set()
        self.right_values=set()


class Solution:
    def dfs(self, root):
        """Return longest overall and longest ending at root."""
        if not root:
            return 0, 0
        l1, l2 = self.dfs(root.left)
        r1, r2 = self.dfs(root.right)
        l2 = 1 + l2 if root.left and root.left.val == root.val else 0
        r2 = 1 + r2 if root.right and root.right.val == root.val else 0
        return max(l1, r1, l2 + r2), max(l2, r2)
    def longestUnivaluePath(self, root):
        return self.dfs(root)[0]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = [5,4,5,1,1,5]
    root = [1, 4, 5, 4, 4, 5]
    root=build_tree(root)
    solution=Solution()
    print(solution.longestUnivaluePath(root))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
