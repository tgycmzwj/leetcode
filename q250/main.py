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
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.count=0
        self.is_unival(root)
        return self.count
    def is_unival(self,node):
        if node.left is None and node.right is None:
            self.count+=1
            return True
        is_uni=True
        if node.left is not None:
            is_uni=(self.is_unival(node.left) and is_uni and node.left.val==node.val)
        if node.right is not None:
            is_uni=(self.is_unival(node.right) and is_uni and node.right.val == node.val)
        self.count+=is_uni
        return is_uni


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = build_tree([5,1,5,5,5,None,5])
    solution=Solution()
    print(solution.countUnivalSubtrees(root))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
