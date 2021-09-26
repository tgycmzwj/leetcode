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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        results=[]
        processing=[]
        if root==None:
            return results
        processing.append([root])
        while len(processing)!=0:
            cur_eles=processing.pop(0)
            next_level_list=[]
            for i in range(len(cur_eles)):
                if cur_eles[i].left:
                    next_level_list.append(cur_eles[i].left)
                if cur_eles[i].right:
                    next_level_list.append(cur_eles[i].right)
                if i==len(cur_eles)-1:
                    results.append(cur_eles[i].val)
            if len(next_level_list)!=0:
                processing.append(next_level_list)
        return results



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = build_tree([1, 2, 3, None, 5, None, 4])
    root=build_tree([1,None,3])
    root=build_tree([])
    solution=Solution()
    print(solution.rightSideView(root))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
