# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def subseq(self,w1,w2):
        i=0
        for c in w2:
            if i<len(w1) and w1[i]==c:
                i+=1
        return i==len(w1)
    def findLUSlength(self, strs: List[str]) -> int:
        strs=sorted(strs,key=lambda x: len(x),reverse=True)
        for i in range(len(strs)):
            if all(not self.subseq(strs[i],word2) for j, word2 in enumerate(strs) if i != j):
                return len(strs[i])
        return -1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    strs = ["aba","cdc","eae"]
    solution=Solution()
    print(solution.findLUSlength(strs))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
