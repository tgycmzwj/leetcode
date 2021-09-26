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


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.root=root
        self.num_list=[]
        self.tranverse(self.root,self.num_list)
        self.num_list.sort()
        self.next_counter=0
    def tranverse(self,root,num_list):
        if root!=None:
            num_list.append(root.val)
            self.tranverse(root.left,num_list)
            self.tranverse(root.right,num_list)
    def next(self) -> int:
        if self.next_counter==0:
            return self.num_list.pop(0)
        else:
            return self.num_list.pop(0)
    def hasNext(self) -> bool:
        return len(self.num_list)>0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmds_content=["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
    cmds_value=[[[7, 3, 15, None, None, 9, 20]], [], [], [], [], [], [], [], [], []]
    results=[]
    for i in range(len(cmds_content)):
        cmd_content=cmds_content[i]
        cmd_value=cmds_value[i]
        if cmd_content=='BSTIterator':
            obj=BSTIterator(build_tree(cmd_value[0]))
            results.append(None)
        elif cmd_content=='next':
            results.append(obj.next())
        elif cmd_content=='hasNext':
            results.append(obj.hasNext())
    print(results)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
