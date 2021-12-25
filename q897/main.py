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
    def inorder(self, root, results):
        if not root: return
        if root.left:
            self.inorder(root.left, results)
        results.append(root.val)
        if root.right:
            self.inorder(root.right, results)

    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root: return None
        results = []
        self.inorder(root, results)
        new_results = [results[0]]
        for i in range(1, len(results)):
            new_results.append(None)
            new_results.append(results[i])
        return build_tree(new_results)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = [5,3,6,2,4,None,8,1,None,None,None,7,9]
    solution=Solution()
    print(solution.increasingBST(root))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
