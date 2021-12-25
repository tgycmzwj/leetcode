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
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        if not root:
            return [None,None]
        elif root.val<=target:
            results=self.splitBST(root.right,target)
            root.right=results[0]
            return [root,results[1]]
        else:
            results=self.splitBST(root.left,target)
            root.left=results[1]
            return [results[0],root]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = [4,2,6,1,3,5,7]
    target = 2
    root=build_tree(root)
    solution=Solution()
    print(solution.splitBST(root,target))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
