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
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        nums=[0]*(n+1)
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 2
        nums[0]=1
        nums[1]=1
        nums[2]=2
        for i in range(2,n+1):
            counter=0
            for point in range(1,i+1):
                num_points_left=point-1
                num_points_right=i-point
                counter=counter+nums[num_points_left]*nums[num_points_right]
            nums[i]=counter
        return nums[-1]





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    for i in range(15):
        print('current i='+str(i))
        print(solution.generateTrees(i))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
