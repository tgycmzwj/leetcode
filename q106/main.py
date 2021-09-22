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
    def buildTree(self, inorder: List[int],postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder)==0:
            return None
        tree_root_value=postorder[-1]
        root=TreeNode(tree_root_value)
        root_num_in_inorder=inorder.index(tree_root_value)

        inorder_left=inorder[:root_num_in_inorder]
        inorder_right=inorder[root_num_in_inorder+1:]
        postorder_left=postorder[:root_num_in_inorder]
        postorder_right=postorder[root_num_in_inorder:len(postorder)-1]
        root.left=self.buildTree(inorder_left,postorder_left)
        root.right=self.buildTree(inorder_right,postorder_right)
        return root




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    solution=Solution()
    print(solution.buildTree(inorder,postorder))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
