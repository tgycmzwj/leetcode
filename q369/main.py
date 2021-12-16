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
    def plusOne(self, head: ListNode) -> ListNode:
        results=[]
        while head:
            results.append(head.val)
            head=head.next
        results=str(int(''.join([str(i) for i in results]))+1)
        results=list(results)
        return build_linked_list(results)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    head = [1, 2, 3]
    head=build_linked_list(head)
    solution=Solution()
    print(solution.plusOne(head))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
