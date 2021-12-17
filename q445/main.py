# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
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
        num1,num2='',''
        while l1:
            num1=num1+str(l1.val)
            l1=l1.next
        while l2:
            num2=num2+str(l2.val)
            l2=l2.next
        results=list(str(int(num1)+int(num2)))
        return build_linked_list([int(i) for i in results])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    l1 = [7,2,4,3]
    l2 = [5,6,4]
    l1=build_linked_list(l1)
    l2=build_linked_list(l2)
    solution=Solution()
    print(solution.addTwoNumbers(l1,l2))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
