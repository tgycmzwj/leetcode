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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        all_routes=[]
        cur_path=[]
        self.bfs(root,cur_path,all_routes)
        return sum([int(''.join(item)) for item in all_routes])
    def bfs(self,root,cur_path,all_routes):
        if root==None:
            return
        cur_path.append(str(root.val))
        if root.left==None and root.right==None:
            all_routes.append(cur_path.copy())
        self.bfs(root.left,cur_path,all_routes)
        self.bfs(root.right,cur_path,all_routes)
        cur_path.pop(-1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = build_tree([4,9,0,5,1])
    solution=Solution()
    print(solution.sumNumbers(root))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
