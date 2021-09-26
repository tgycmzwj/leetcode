# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List,Optional
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
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        list=[]
        while head is not None:
            if head.val!=val:
                list.append(head.val)
            head=head.next
        return build_linked_list(list)





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    head = build_linked_list([6, 1, 2, 6, 3, 4, 5, 6])
    val = 6
    solution=Solution()
    print(solution.removeElements(head,val))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
