# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        canreach=[(0,nums[0])]
        cur_farthest=0
        while len(canreach)>0:
            cur_pos,cur_val=canreach.pop(0)

            for i in range(cur_farthest+1,min(len(nums),cur_val+cur_pos+1)):
                if (i,nums[i]) not in canreach:
                    canreach.append((i,nums[i]))
            cur_farthest=cur_val+cur_pos
            if cur_farthest>=len(nums)-1:
                return True
        return False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    nums=[4,1,4,5,4,2,1,6,5,4,6,4,1,4,2,3,4,2,5,2,2,1,5,3,3,6,3,4,1,1,2,4,6,6,3,6,3,5,4,2,2,4,3,1,2,3,6,5,2,6,3,1,1,3,2,2,1,5,4,2,6,4,4,5,6,4,6,2,1,6,4,2,5,6,2,1,5,2,6,1,3,2,5,2,6,5,1,5,5,3,4,6,6,3,4,4,1,6,5,1,1,6,2,6,1,1,5,4,4,4,5,5,3,3,5,5,5,2,6,2,2,5,1,6,6,2,5,1,6,1,5,5,5,1,5,1,6,2,2,6,6,1,6,2,6,5,1,1,6,2,6,3,4,2,1,6,4,5,6,2,6,4,2,6,3,1,4,5,1,6,5,1,4,4,6,2,2,5,6,1,4,5,4,1,5,4,3,2,5,6,5,2,2,4,5,2,2,4,4,3,6,1,5,1,2,1,6,2,5,6,1,2,3,2,6,6,5,6,1,6,6,1,2,2,2,5,5,1,2,4,5,2,1,4,1,5,4,5,4,3,3,3,5,4,6,3,6,4,4,4,4,1,4,4,3,1,4,4,4,2,3,5,5,6,4,6,5,1,5,4,5,5,2,3,4,2,3,2,5,6,1,4,3,2,4,3,4,6,0,0,0,0,0,0]
    print(solution.canJump(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
