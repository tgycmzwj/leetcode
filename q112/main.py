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


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None and root.val==targetSum:
            return True
        return max(self.hasPathSum(root.left,targetSum-root.val),self.hasPathSum(root.right,targetSum-root.val))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = build_tree([5,4,8,11,None,13,4,7,2,None,None,None,1])
    targetSum = 22
    # root = build_tree([1, 2, 3])
    # targetSum = 5
    # root = build_tree([1, 2])
    # targetSum = 0
    solution=Solution()
    print(solution.hasPathSum(root,targetSum))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
