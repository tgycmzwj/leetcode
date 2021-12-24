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
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        listn=[]
        results=[]
        while head:
            results.append(head.val)
            head=head.next
        leng=len(results)//k
        remainder=len(results)-k*leng
        for i in range(k):
            if i<remainder:
                cur=results[:leng+1]
                listn.append(build_linked_list(cur))
                results=results[leng+1:]
            else:
                cur=results[:leng]
                listn.append(build_linked_list(cur))
                results=results[leng:]
        return listn

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    head = [1,2,3,4,5,6,7,8,9,10,11]
    k = 3
    head=build_linked_list(head)
    solution=Solution()
    print(solution.splitListToParts(head,k))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
