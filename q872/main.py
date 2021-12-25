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
    def get_leaves(self,root,results):
        if not root:
            return
        if not root.left and not root.right:
            results.append(root.val)
        if root.left:
            self.get_leaves(root.left,results)
        if root.right:
            self.get_leaves(root.right,results)
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1=[]
        leaves2=[]
        self.get_leaves(root1,leaves1)
        self.get_leaves(root2,leaves2)
        if leaves1==leaves2:
            return True
        return False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root1 = [3,5,1,6,2,9,8,None,None,7,4]
    root2 = [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]
    root1 = [1, 2, 3]
    root2 = [1, 3, 2]
    root1=build_tree(root1)
    root2=build_tree(root2)
    solution=Solution()
    print(solution.leafSimilar(root1,root2))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
