# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if (head == None or head.next == None):
            return head
        prev = head
        curr = head.next
        curr1 = curr
        head = curr
        while True:
            next_node = curr.next
            curr.next = prev
            if (next_node == None or next_node.next == None):
                prev.next = next_node
                break
            prev.next = next_node.next
            prev = next_node
            curr = next_node.next
        return curr1


    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    head = [1, 2, 3, 4]
    print(solution.swapPairs(head))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
