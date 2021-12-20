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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        results=[]
        process=[root]
        while len(process)>0:
            cur_root=process.pop(0)
            self.dfs(cur_root,targetSum,0,[],results)
            if cur_root.left:
                process.append(cur_root.left)
            if cur_root.right:
                process.append(cur_root.right)
        return len(results)
    def dfs(self,root,targetSum,running_sum,cur_list,results):
        if root is None:
            return
        cur_list.append(root.val)
        running_sum=running_sum+root.val
        if running_sum==targetSum:
            results.append(cur_list.copy())
        self.dfs(root.left,targetSum,running_sum,cur_list,results)
        self.dfs(root.right,targetSum,running_sum,cur_list,results)
        cur_list.pop(-1)
        running_sum=running_sum-root.val

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = [10,5,-3,3,2,None,11,3,-2,None,1]
    targetSum = 8
    root=build_tree(root)
    solution=Solution()
    print(solution.pathSum(root,targetSum))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
