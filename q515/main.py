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
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        processing=[[root]]
        results=[]
        while len(processing)>0:
            cur_level=processing.pop(0)
            next_level=[]
            val=-1e15
            for sub in cur_level:
                val=max(val,sub.val)
                if sub.left:
                    next_level.append(sub.left)
                if sub.right:
                    next_level.append(sub.right)
            results.append(val)
            if len(next_level)>0:
                processing.append(next_level.copy())
        return results



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = [1,3,2,5,3,None,9]
    root=build_tree(root)
    solution=Solution()
    print(solution.largestValues(root))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
