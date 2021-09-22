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
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        results=[]
        processing=[[root]]
        while len(processing)!=0:
            items=processing.pop(0)
            processing_to_be_append=[]
            results_to_be_append=[]
            for item in items:
                results_to_be_append.append(item.val)
                if item.left:
                    processing_to_be_append.append(item.left)
                if item.right:
                    processing_to_be_append.append(item.right)
            results.append(results_to_be_append)
            if len(processing_to_be_append)!=0:
                processing.append(processing_to_be_append)
        results.reverse()
        return results

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = build_tree([3,9,20,None,None,15,7])
    solution=Solution()
    print(solution.levelOrder(root))