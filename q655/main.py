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

import math
class Solution:
    def depth(self,root):
        if not root:
            return 0
        return max(self.depth(root.left),self.depth(root.right))+1
    def insert(self,node,low,high,output,depth=0):
        if not node:
            return
        mid=(low+high)//2
        output[depth][mid]=str(node.val)
        self.insert(node.left,low,mid,output,depth+1)
        self.insert(node.right,mid,high,output,depth+1)
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        depth=self.depth(root)
        output=[['']*(2**depth-1) for i in range(depth)]
        self.insert(root,0,2**depth-1,output,depth=0)
        return output





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = [1,2,3,None,4]
    root=build_tree(root)
    solution=Solution()
    print(solution.printTree(root))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
