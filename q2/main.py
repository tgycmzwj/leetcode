# Definition for singly-linked list.
from typing import Optional
from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def build_linked_list(l:List)->Optional[ListNode]:
    if len(l)==0:
        return
    node=ListNode(l[0])
    cur_node=node
    for i in l[1:]:
        cur_node.next=ListNode(i)
        cur_node=cur_node.next
    return node

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1=0
        num2=0
        counter1=0
        counter2=0
        while l1!=None:
            num1=num1+pow(10,counter1)*l1.val
            l1=l1.next
            counter1=counter1+1
        while l2!=None:
            num2=num2+pow(10,counter2)*l2.val
            l2=l2.next
            counter2=counter2+1
        results=str(num1+num2)
        return_list = []
        node_start = ListNode(results[-1])
        node_tmp=node_start
        for i in range(1, len(results)):
            node_tmp.next = ListNode(results[len(results) - i - 1])
            node_tmp = node_tmp.next
        return node_start

if __name__=='__main__':
    solution=Solution()
    test=build_linked_list([2,3,4,5])
    print(solution.addTwoNumbers([2,4,3], [5,6,4]))