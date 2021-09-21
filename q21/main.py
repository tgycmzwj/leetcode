# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1 is None and l2 is None:
            return None
        else:

            l3 = last = None

            if l1.val < l2.val:
                l3 = last = l1
                l1 = l1.next
                last.next = None
            else:
                l3 = last = l2
                l2 = l2.next
                last.next = None

            while l1 and l2:
                if l1.val < l2.val:
                    last.next = l1
                    last = l1
                    l1 = l1.next
                    last.next = None
                else:
                    last.next = l2
                    last = l2
                    l2 = l2.next
                    last.next = None

            if l1:
                last.next = l1
            else:
                last.next = l2

            return l3


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    l1 = [1,2,4]
    l2 = [1,3,4]
    solution=Solution()
    print(solution.mergeTwoLists(l1,l2))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
