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
    def same(self,root1,root2):
        if not root1 and not root2:
            return True
        if (not root1 and root2) or (root1 and not root2):
            return False
        if root1.val!=root2.val:
            return False
        left_same=self.same(root1.left,root2.left)
        right_same=self.same(root1.right,root2.right)
        return min(left_same,right_same)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        processing=[root]
        while len(processing)>0:
            cur_ele=processing.pop(0)
            if self.same(cur_ele,subRoot):
                return True
            if cur_ele.left:
                processing.append(cur_ele.left)
            if cur_ele.right:
                processing.append(cur_ele.right)
        return False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = [3,4,5,1,2,None,None,None,None,0]
    subRoot = [4,1,2]
    root=build_tree(root)
    subRoot=build_tree(subRoot)
    solution=Solution()
    print(solution.isSubtree(root,subRoot))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
