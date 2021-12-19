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
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth==1:
            temp=TreeNode(val)
            temp.left=root
            return temp
        copy=root
        processed=[]
        process=[[copy]]
        while len(process)>0:
            cur_level=process.pop(0)
            new_level=[]
            processed.append(cur_level)
            if len(processed)==depth-1:
                for cur_ele in cur_level:
                    temp_left = cur_ele.left
                    cur_ele.left=TreeNode(val)
                    if temp_left:
                        cur_ele.left.left=temp_left
                    temp_right=cur_ele.right
                    cur_ele.right=TreeNode(val)
                    if temp_right:
                        cur_ele.right.right=temp_right
                break
            for cur_ele in cur_level:
                if cur_ele.left:
                    new_level.append(cur_ele.left)
                if cur_ele.right:
                    new_level.append(cur_ele.right)
            process.append(new_level.copy())
        return root


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = [4,2,6,3,1,5]
    val = 1
    depth = 2
    root=build_tree(root)
    solution=Solution()
    print(solution.addOneRow(root,val,depth))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
