# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            if strs[i]<strs[i][::-1]:
                strs[i]=strs[i][::-1]
        ans = ''
        for i, token in enumerate(strs):
            for start in (token,token[::-1]):
                #split the current word
                for j in range(len(start)+1):
                    ans=max(ans,start[j:]+"".join(strs[i+1:]+strs[:i])+start[:j])
        return ans

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    strs = ["abc","xyz"]
    solution=Solution()
    print(solution.splitLoopedString(strs))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
