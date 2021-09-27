# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from typing import List
from typing import Optional
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
    def build_linked_list(self, l: List) -> Optional[ListNode]:
        if len(l) == 0:
            return
        node = ListNode(l[0])
        cur_node = node
        for i in l[1:]:
            cur_node.next = ListNode(i)
            cur_node = cur_node.next
        return node

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return head

        results = []
        traverse = head
        while traverse is not None:
            results.append(traverse.val)
            traverse = traverse.next
        new_results = []
        while len(results) > 1:
            new_results.append(results.pop(0))
            new_results.append(results.pop())
        if len(results) != 0:
            new_results.append(results.pop())

        head_copy = head
        while head_copy is not None:
            head_copy.val = new_results.pop(0)
            head_copy = head_copy.next


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    head = build_linked_list([1, 2, 3, 4, 5])
    solution=Solution()
    print(solution.reorderList(head))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
