# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if k == 0:
            return head
        i = 0
        cur = head
        pre = None
        while cur:
            pre = cur
            cur = cur.next
            i += 1
        s = k % i

        position = 1
        cur = head
        while position < i - s:
            cur = cur.next
            position += 1
        p = cur.next
        if p:
            cur.next = None
            pre.next = head
            return p
        return head

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
