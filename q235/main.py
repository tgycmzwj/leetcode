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
    def diff_side(self,cutoff,p,q):
        if (p.val<cutoff and q.val>cutoff) or (p.val>cutoff and q.val<cutoff) or (p.val==cutoff) or (q.val==cutoff):
            return True
        return False
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        tree=root
        if self.diff_side(tree.val,p,q):
            return tree.val
        if p.val<tree.val:
            return self.lowestCommonAncestor(root.left,p,q)
        if p.val>tree.val:
            return self.lowestCommonAncestor(root.right,p,q)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = build_tree([6,2,8,0,4,7,9,None,None,3,5])
    p = TreeNode(2)
    q = TreeNode(8)
    # root = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    # p = TreeNode(2)
    # q = TreeNode(4)
    # root = build_tree([2, 1])
    # p = TreeNode(2)
    # q = TreeNode(1)
    solution=Solution()
    print(solution.lowestCommonAncestor(root,p,q))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
