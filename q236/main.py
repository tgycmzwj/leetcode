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
    def pre_tran(self,root,results):
        if root is None:
            return
        results.append(root.val)
        self.pre_tran(root.left,results)
        self.pre_tran(root.right,results)
    def mid_tran(self,root,results):
        if root is None:
            return
        self.mid_tran(root.left,results)
        results.append(root.val)
        self.mid_tran(root.right,results)
    def diff_branch(self,left,right,cur_root,p,q):
        if ((p==cur_root) or (q==cur_root) or (p in left and q in right) or (p in right and q in left)):
            return True
        return False
    def find_root(self,root,root_value):
        if root==None:
            return
        if root.val==root_value:
            return root
        if self.find_root(root.left,root_value):
            return self.find_root(root.left,root_value)
        return self.find_root(root.right,root_value)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pre_results,mid_results=[],[]
        self.pre_tran(root,pre_results)
        self.mid_tran(root,mid_results)
        cur_root=pre_results[0]

        index_in_mid=mid_results.index(cur_root)

        left_mid=mid_results[:index_in_mid]
        right_mid=mid_results[index_in_mid+1:]
        left_pre=pre_results[1:len(left_mid)+1]
        right_pre=pre_results[len(left_mid)+1:]
        while self.diff_branch(left_mid,right_mid,cur_root,p,q)==False:
            if p in left_mid:
                cur_root=left_pre[0]
                index_in_mid = left_mid.index(cur_root)
                left_mid,right_mid = left_mid[:index_in_mid],left_mid[index_in_mid + 1:]
                left_pre,right_pre = left_pre[1:len(left_mid) + 1],left_pre[len(left_mid) + 1:]
            elif p in right_mid:
                cur_root=right_pre[0]
                index_in_mid = right_mid.index(cur_root)
                left_mid,right_mid = right_mid[:index_in_mid],right_mid[index_in_mid + 1:]
                left_pre,right_pre = right_pre[1:len(left_mid) + 1],right_pre[len(left_mid) + 1:]
        return self.find_root(root,cur_root)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p = 5
    q = 4
    # root = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    # p = 2
    # q = 4
    # root = build_tree([1, 2])
    # p = 1
    # q = 2
    solution=Solution()
    print(solution.lowestCommonAncestor(root,p,q))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
