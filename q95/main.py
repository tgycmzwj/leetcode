# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# Definition for a binary tree node.
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
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n==0:
            return []
        return self.tree_generator(1,n)
    def tree_generator(self,start,end):
        if start>end:
            return [None]
        all_trees=[]
        for Root_value in range(start,end+1):
            #left part of the tree
            left_subtrees=self.tree_generator(start,Root_value-1)
            #right part of the tree
            right_subtrees=self.tree_generator(Root_value+1,end)
            for left_subtree in left_subtrees:
                for right_subtree in right_subtrees:
                    root_node=TreeNode(Root_value)
                    root_node.left=left_subtree
                    root_node.right=right_subtree
                    all_trees.append(root_node)
        return all_trees



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n=3
    solution=Solution()
    print(solution.generateTrees(3))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
