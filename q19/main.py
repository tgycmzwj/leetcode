# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l1 = head
        l2 = head
        k = n
        while k != 0:
            l2 = l2.next
            k = k - 1
        if l2 != None:
            while l2.next != None:
                l1 = l1.next
                l2 = l2.next
        else:
            return l1.next
        l1.next = l1.next.next
        return head


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    head = [1, 2, 3, 4, 5]
    n = 2
    print(solution.removeNthFromEnd(head,n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
