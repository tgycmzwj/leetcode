# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.



from typing import Optional
from typing import List
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = None
def build_node(s):
    if len(s)==0:
        return
    root=Node(s[0])
    s.pop(0)
    ongoing_list=[root]
    while len(ongoing_list)!=0:
        cur_node=ongoing_list.pop(0)
        while cur_node.val==None:
             cur_node=ongoing_list.pop(0)
        if len(s)!=0:
            left_node=Node(s.pop(0))
        else:
            break
        if left_node.val!=None:
            cur_node.left = left_node
            ongoing_list.append(left_node)
        if len(s)!=0:
            right_node=Node(s.pop(0))
        else:
            break
        if right_node.val!=None:
            cur_node.right=right_node
            ongoing_list.append(right_node)
    return root


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root==None:
            return root
        processing=[[root]]
        while len(processing)!=0:
            cur_eles=processing.pop(0)
            future_eles=[]
            if len(cur_eles)==1:
                if cur_eles[0].left:
                    future_eles.append(cur_eles[0].left)
                if cur_eles[0].right:
                    future_eles.append(cur_eles[0].right)
                if len(future_eles)!=0:
                    processing.append(future_eles)
            else:
                for i in range(len(cur_eles)-1):
                    #append
                    if cur_eles[i].left:
                        future_eles.append(cur_eles[i].left)
                    if cur_eles[i].right:
                        future_eles.append(cur_eles[i].right)
                    #append more
                    if i==len(cur_eles)-2:
                        if cur_eles[i+1].left:
                            future_eles.append(cur_eles[i+1].left)
                        if cur_eles[i+1].right:
                            future_eles.append(cur_eles[i+1].right)
                    #next
                    cur_eles[i].next=cur_eles[i+1]
                if len(future_eles)!=0:
                    processing.append(future_eles)
        return root




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = build_node([1,2,3,4,5,6,7])
    solution=Solution()
    print(solution.connect(root))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
