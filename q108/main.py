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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums)==0:
            return None
        mid_point=len(nums)//2
        mid_node=nums[mid_point]
        root=TreeNode(mid_node)
        left_nodes=nums[:mid_point]
        right_nodes=nums[mid_point+1:]
        root.left=self.sortedArrayToBST(left_nodes)
        root.right=self.sortedArrayToBST(right_nodes)
        return root


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [0,1,2,3,4,5]
    solution=Solution()
    print(solution.sortedArrayToBST(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
