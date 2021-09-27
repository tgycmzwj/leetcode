# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List,Optional
import copy
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        return copy.deepcopy(head)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    head =[[7,None],[13,0],[11,4],[10,2],[1,0]]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
