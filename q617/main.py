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
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if (not root1):
            return root2
        if (not root2):
            return root1
        root1.val=root1.val+root2.val
        root1.left=self.mergeTrees(root1.left,root2.left)
        root1.right=self.mergeTrees(root1.right,root2.right)
        return root1



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root1 = [1,3,2,5]
    root2 = [2,1,3,None,4,None,7]
    root1=build_tree(root1)
    root2=build_tree(root2)
    solution=Solution()
    print(solution.mergeTrees(root1,root2))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
