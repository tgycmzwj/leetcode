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
    def depth(self,node:Optional[TreeNode])->int:
        if not node:
            return 0
        return max(self.depth(node.left),self.depth(node.right))+1
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        process=[root]
        cur_max=0
        while len(process)!=0:
            cur_node=process.pop(0)
            cur_max=max(cur_max,self.depth(cur_node.left)+self.depth(cur_node.right))
            if cur_node.left:
                process.append(cur_node.left)
            if cur_node.right:
                process.append(cur_node.right)
        return cur_max



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = [1,2,3,4,5]
    root=[4,-7,-3,None,None,-9,-3,9,-7,-4,None,6,None,-6,-6,None,None,0,6,5,None,9,None,None,-1,-4,None,None,None,-2]
    root=build_tree(root)
    solution=Solution()
    print(solution.diameterOfBinaryTree(root))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
