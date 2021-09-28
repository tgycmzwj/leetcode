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
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_depth= self.get_depth(root.left)
        right_depth = self.get_depth(root.right)
        if left_depth==right_depth:
            return 2**left_depth+self.countNodes(root.right)
        else:
            return 2**right_depth+self.countNodes(root.left)
    def get_depth(self,root:Optional[TreeNode])->int:
        counter=0
        while root is not None:
            counter=counter+1
            root=root.left
        return counter



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = build_tree([1, 2, 3, 4, 5, 6])
    solution=Solution()
    print(solution.countNodes(root))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
