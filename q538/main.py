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
    def inorder(self,root:Optional[TreeNode],results)->List[int]:
        if not root:
            return
        self.inorder(root.left,results)
        results.append(root.val)
        self.inorder(root.right,results)
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        results=[]
        self.inorder(root,results)
        dic={}
        sums=[0]*len(results)
        sums[-1]=results[-1]
        dic[results[-1]]=sums[-1]
        for i in range(len(results)-2,-1,-1):
            sums[i]=sums[i+1]+results[i]
            dic[results[i]]=sums[i]
        copy=root
        process=[copy]
        while len(process)!=0:
            cur_ele=process.pop(0)
            cur_ele.val=dic[cur_ele.val]
            if cur_ele.left:
                process.append(cur_ele.left)
            if cur_ele.right:
                process.append(cur_ele.right)
        return root





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
    root=build_tree(root)
    solution=Solution()
    print(solution.convertBST(root))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
