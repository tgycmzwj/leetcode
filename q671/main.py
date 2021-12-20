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
        self.inorder(root.left, results)
        results.append(root.val)
        self.inorder(root.right, results)

    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        results = []
        self.inorder(root, results)
        results.sort()
        min_val = results[0]
        for i in range(1, len(results)):
            if results[i] != min_val:
                return results[i]
        return -1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root=[5,8,5]
    root=build_tree(root)
    solution=Solution()
    print(solution.findSecondMinimumValue(root))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
