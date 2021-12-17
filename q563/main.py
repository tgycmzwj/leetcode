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
    def sum_of_tree(self,node:Optional[TreeNode])->int:
        if not node:
            return 0
        cur_sum=0
        process=[node]
        while len(process)!=0:
            cur_ele=process.pop(0)
            cur_sum=cur_sum+cur_ele.val
            if cur_ele.left:
                process.append(cur_ele.left)
            if cur_ele.right:
                process.append(cur_ele.right)
        return cur_sum
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        process=[root]
        results=0
        while len(process)!=0:
            cur_ele=process.pop(0)
            results=results+abs(self.sum_of_tree(cur_ele.left)-self.sum_of_tree(cur_ele.right))
            if cur_ele.left:
                process.append(cur_ele.left)
            if cur_ele.right:
                process.append(cur_ele.right)
        return results



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = [4,2,9,3,5,None,7]
    root=build_tree(root)
    solution=Solution()
    print(solution.findTilt(root))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
