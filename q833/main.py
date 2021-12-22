# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        for index, source, target in sorted(zip(indexes,sources,targets), reverse= True):
            if S[index:index+len(source)] == source:
                S = S[:index] + target + S[index+len(source):]
        return S

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "abcd"
    indices = [0, 2]
    sources = ["ab","ec"]
    targets = ["eee","ffff"]
    solution=Solution()
    print(solution.findReplaceString(s,indices,sources,targets))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
