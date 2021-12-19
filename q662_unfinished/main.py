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
    def transform(self,nums):
        results=''
        for i in nums:
            if i:
                results=results+'1'
            else:
                results=results+'0'
        return results.strip('0')
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        process=[[root]]
        results=[]
        i=0
        while len(process)>0:
            i=i+1
            print(i)
            new_level=[]
            cur_results=[]
            cur_level=process.pop(0)
            for cur_ele in cur_level:
                if cur_ele:
                    cur_results.append(cur_ele.val)
                    new_level.append(cur_ele.left)
                    new_level.append(cur_ele.right)
                else:
                    cur_results.append(None)
                    new_level.append(None)
                    new_level.append(None)
            if (len(set(new_level))>1) or (len(set(new_level))==1 and None not in set(new_level)):
                process.append(new_level.copy())
            results.append(cur_results.copy())
        return max([len(self.transform(i)) for i in results])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = [1,3,2,5,3,None,9]
    root = [1, 3, None, 5, 3]
    root = [1, 3, 2, 5]
    root=[1]
    root = [1, 3, 2, 5, None, None, 9, 6, None, None, 7]
    root=build_tree(root)
    solution=Solution()
    print(solution.widthOfBinaryTree(root))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/