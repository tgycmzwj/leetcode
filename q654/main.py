# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import Optional
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def breakdown(self,nums:List[int]):
        max_index=nums.index(max(nums))
        small=nums[:max_index]
        large=nums[max_index+1:]
        return [small,nums[max_index],large]
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        parts=self.breakdown(nums)
        root=TreeNode(parts[1])
        if len(parts[0])==0:root.left=None
        else:root.left=self.constructMaximumBinaryTree(parts[0])
        if len(parts[2])==0:root.right=None
        else:root.right=self.constructMaximumBinaryTree(parts[2])
        return root




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [3,2,1,6,0,5]
    solution=Solution()
    print(solution.constructMaximumBinaryTree(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
