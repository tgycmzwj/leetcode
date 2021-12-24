# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
class Solution:
    def traverse(self,processing,results):
        while len(processing)!=0:
            cur_level=processing.pop(0)
            new_level_nodes=[]
            cur_level_value=[]
            for cur_ele in cur_level:
                cur_level_value.append(cur_ele.val)
                for child in cur_ele.children:
                    if child:
                        new_level_nodes.append(child)
            if len(new_level_nodes)>0:
                processing.append(new_level_nodes.copy())
            results.append(cur_level_value.copy())


    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:return []
        processing=[[root]]
        results=[]
        self.traverse(processing,results)
        return results


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = [1,None,3,2,4,None,5,6]
    solution=Solution()
    print(solution.levelOrder(root))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
