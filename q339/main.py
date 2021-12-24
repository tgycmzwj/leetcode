# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class Solution:
    def dfs(self,ni, depth):
        if ni.isInteger():
            return depth*ni.getInteger()
        return sum(self.dfs(n,depth+1) for n in ni.getList())
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        return sum(self.dfs(ni,1) for ni in nestedList)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nestedList = [1,[4,[6]]]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
