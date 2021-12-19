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
    def traverse(self, root, all_ele, dic):
        if not root:
            return
        self.traverse(root.left, all_ele, dic)
        all_ele.append(root.val)
        if root.val not in dic.keys():
            dic[root.val] = 1
        else:
            dic[root.val] = 2
        self.traverse(root.right, all_ele, dic)

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        all_ele = []
        dic = {}
        self.traverse(root, all_ele, dic)
        all_ele_set = set(all_ele)
        for i in all_ele:
            if k - i in all_ele_set:
                if k - i != i:
                    return True
                if dic[i] == 2:
                    return True
        return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = [5,3,6,2,4,None,7]
    k = 9
    solution=Solution()
    print(solution.findTarget(root,k))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
