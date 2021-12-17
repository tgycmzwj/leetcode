# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for num in nums:
            self.add(num)  # add elements using the function below
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]  # the root element



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmds=["KthLargest", "add", "add", "add", "add", "add"]
    vals=[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
    results=[]
    for i in range(len(cmds)):
        cmd,val=cmds[i],vals[i]
        if cmd=='KthLargest':
            obj=KthLargest(val[0],val[1])
            results.append(None)
        elif cmd=='add':
            results.append(obj.add(val[0]))
    print(results)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
