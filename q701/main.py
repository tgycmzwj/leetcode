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
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node=root
        while node:
            #need to insert to the right
            if val>node.val:
                if not node.right:
                    node.right=TreeNode(val)
                    return root
                else:
                    node=node.right
            #need to insert to the left
            else:
                if not node.left:
                    node.left=TreeNode(val)
                    return root
                else:
                    node=node.left
        return TreeNode(val)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = [4,2,7,1,3]
    val = 5
    root=build_tree(root)
    solution=Solution()
    print(solution.insertIntoBST(root,val))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
