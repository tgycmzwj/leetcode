# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None,head)
        prev = dummy
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                val = curr.val
                while curr and curr.val == val:
                    curr = curr.next
                prev.next = curr
            else:
                curr = curr.next
                prev = prev.next
        return dummy.next

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
