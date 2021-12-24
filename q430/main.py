# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import Optional
from typing import List

class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def build_linked_list(l: List) -> Optional[Node]:
    if len(l) == 0:
        return
    node = Node(l[0])
    cur_node = node
    for i in l[1:]:
        cur_node.next = Node(i)
        temp = cur_node.next
        temp.prev = cur_node
        cur_node = temp
    return node


class Solution:
    def flat(self, head, results):
        if not head: return
        results.append(head.val)
        self.flat(head.child, results)
        self.flat(head.next, results)

    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        results = []
        self.flat(head, results)
        return build_linked_list(results)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    head = [1,2,3,4,5,6,None,None,None,7,8,9,10,None,None,11,12]
    head=build_linked_list(head)
    solution=Solution()
    print(solution.flatten(head))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
