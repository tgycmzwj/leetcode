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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)==0:
            return None
        tree_root_value=preorder[0]
        root=TreeNode(tree_root_value)
        root_num_in_inorder=inorder.index(tree_root_value)

        inorder_left=inorder[:root_num_in_inorder]
        inorder_right=inorder[root_num_in_inorder+1:]
        preorder_left=preorder[1:1+root_num_in_inorder]
        preorder_right=preorder[1+root_num_in_inorder:]
        root.left=self.buildTree(preorder_left,inorder_left)
        root.right=self.buildTree(preorder_right,inorder_right)
        return root




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    solution=Solution()
    print(solution.buildTree(preorder,inorder))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
