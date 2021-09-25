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
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre=head
        while pre.next!=None:
            post=pre.next
            while post!=None:
                if pre.val>post.val:
                    temp=pre.val
                    pre.val=post.val
                    post.val=temp
                post=post.next
            pre=pre.next
        return head


# Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    head=build_linked_list([-1,5,3,4,0])
    solution=Solution()
    print(solution.insertionSortList(head))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
