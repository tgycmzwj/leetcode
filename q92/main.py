# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution(object):
    def reverseBetween(self, head, m, n):
        if m >= n:
            return head
        # Step 1#
        ohead = dummy = ListNode(0)
        whead = wtail = head
        dummy.next = head
        for i in range(n - m):
            wtail = wtail.next
        # Step 2#
        for i in range(m - 1):
            ohead, whead, wtail = whead, whead.next, wtail.next
        # Step 3#
        otail, wtail.next = wtail.next, None
        revhead, revtail = self.reverse(whead)
        # Step 4#
        ohead.next, revtail.next = revhead, otail
        return dummy.next

    def reverse(self, head):
        pre, cur, tail = None, head, head
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre, tail
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
