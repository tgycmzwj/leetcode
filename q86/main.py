# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummyLess, dummyMore = ListNode(), ListNode()
        less, more = dummyLess, dummyMore

        while head:
            if head.val < x:
                less.next = head
                less, head = less.next, head.next
            else:
                more.next = head
                more, head = more.next, head.next

        more.next = None  # clear the tail pointer
        less.next = dummyMore.next
        return dummyLess.next

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
