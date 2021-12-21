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

class TreeNode_cust(TreeNode):
    def __init__(self,root):
        super(TreeNode_cust, self).__init__()
        self.val=root.val
        if root.left:self.left=TreeNode_cust(root.left)
        if root.right:self.right=TreeNode_cust(root.right)
        self.left_sum=0
        self.right_sum=0


class Solution:
    def cal_sum(self,root_new):
        if not root_new.left and not root_new.right:
            root_new.left_sum=0
            root_new.right_sum=0
        if not root_new.left and root_new.right:
            root_new.left_sum=0
            self.cal_sum(root_new.right)
            root_new.right_sum=root_new.right.left_sum+root_new.right.right_sum+root_new.right.val
        if not root_new.right and root_new.left:
            root_new.right_sum=0
            self.cal_sum(root_new.left)
            root_new.left_sum=root_new.left.left_sum+root_new.left.right_sum+root_new.left.val
        if root_new.right and root_new.left:
            self.cal_sum(root_new.left)
            self.cal_sum(root_new.right)
            root_new.right_sum = root_new.right.left_sum + root_new.right.right_sum + root_new.right.val
            root_new.left_sum = root_new.left.left_sum + root_new.left.right_sum + root_new.left.val
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        root_new=TreeNode_cust(root)
        self.cal_sum(root_new)
        dic={root_new.left_sum+root_new.right_sum+root_new.val:1}
        process=[root_new]
        while len(process)>0:
            cur_ele=process.pop(0)
            if cur_ele.left:
                if cur_ele.left_sum not in dic:
                    dic[cur_ele.left_sum]=0
                dic[cur_ele.left_sum]+=1
                process.append(cur_ele.left)
            if cur_ele.right:
                if cur_ele.right_sum not in dic:
                    dic[cur_ele.right_sum]=0
                dic[cur_ele.right_sum]+=1
                process.append(cur_ele.right)
        cur_max=0
        for k,v in dic.items():
            cur_max=max(cur_max,v)
        results=[]
        for k,v in dic.items():
            if v==cur_max:
                results.append(k)
        return results


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = [5,2,-3]
    root=[5, 2, -5]
    root=build_tree(root)
    solution=Solution()
    print(solution.findFrequentTreeSum(root))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
