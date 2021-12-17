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
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic={}
        if root==None:
            return []
        process=[root]
        while len(process)>0:
            cur_ele=process.pop(0)
            if cur_ele.val not in dic:
                dic[cur_ele.val]=1
            else:
                dic[cur_ele.val]=dic[cur_ele.val]+1
            if cur_ele.left:
                process.append(cur_ele.left)
            if cur_ele.right:
                process.append(cur_ele.right)
        results=[]
        cur_max=0
        for k,v in dic.items():
            if v>cur_max:
                results=[k]
                cur_max=v
            elif v==cur_max:
                results.append(k)
        return results



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root =[-2,-2,-2]
    root=build_tree(root)
    solution=Solution()
    print(solution.findMode(root))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
