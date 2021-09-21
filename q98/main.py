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
    def extra_extre(self,root:Optional[TreeNode])->bool:
        cur_min=root.val
        cur_max=root.val
        subs=[root.left,root.right]
        subs=[item for item in subs if item is not None]
        while len(subs)!=0:
            cur_ele=subs.pop(0)
            cur_min=min(cur_min,cur_ele.val)
            cur_max=max(cur_max,cur_ele.val)
            if cur_ele.left is not None:
                subs.append(cur_ele.left)
            if cur_ele.right is not None:
                subs.append(cur_ele.right)
        return cur_min,cur_max


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if root.left is not None:
            if self.extra_extre(root.left)[1]>=root.val:
                return False
            if self.isValidBST(root.left)==False:
                return False
        if root.right is not None:
            if self.extra_extre(root.right)[0]<=root.val:
                return False
            if self.isValidBST(root.right)==False:
                return False
        return True



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = build_tree([1,None,1])
    solution=Solution()
    print(solution.isValidBST(root))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
