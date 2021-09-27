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
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None

        pa = headA # 2 pointers
        pb = headB

        while pa is not pb:
            # if either pointer hits the end, switch head and continue the second traversal,
            # if not hit the end, just move on to next
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa # only 2 ways to get out of the loop, they meet or the both hit the end=None




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    listA = build_linked_list([4, 1, 8, 4, 5])
    listB = build_linked_list([5, 6, 1, 8, 4, 5])
    solution=Solution()
    print(solution.getIntersectionNode(listA,listB))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
