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
    def build_linked_list(self,l: List) -> Optional[ListNode]:
        if len(l) == 0:
            return
        node = ListNode(l[0])
        cur_node = node
        for i in l[1:]:
            cur_node.next = ListNode(i)
            cur_node = cur_node.next
        return node
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        results_list=[]
        while head:
            results_list.append(head.val)
            head=head.next
        results_list.reverse()
        return self.build_linked_list(results_list)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    head = build_linked_list([1, 2, 3, 4, 5])
    solution=Solution()
    print(solution.reverseList(head))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
