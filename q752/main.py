# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        target=tuple([int(i) for i in target])
        deadends=[tuple([int(j) for j in i]) for i in deadends]
        directions=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
        processing=[[(0,0,0,0)]]
        processed=set()
        i=0
        while len(processing)>0:
            cur_step=processing.pop(0)
            new_step=[]
            if target in cur_step:
                return i
            for cur_ele in cur_step:
                processed.add(cur_ele)
                for di in directions:
                    for sign in [1,-1]:
                        new_ele=((cur_ele[0]+sign*di[0]+10)%10,(cur_ele[1]+sign*di[1]+10)%10,(cur_ele[2]+sign*di[2]+10)%10,(cur_ele[3]+sign*di[3]+10)%10)
                        if new_ele not in deadends and new_ele not in processing and new_ele not in processed:
                            new_step.append(new_ele)
            processing.append(new_step)
            i=i+1
        return -1



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
    target = "8888"
    deadends = ["0201", "0101", "0102", "1212", "2002"]
    target = "0202"
    solution=Solution()
    print(solution.openLock(deadends,target))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
