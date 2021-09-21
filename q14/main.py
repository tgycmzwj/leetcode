# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length=min([len(i) for i in strs])

        for i in range(1,min_length+1):
            if len(set([str_ele[:i] for str_ele in strs]))!=1:
                return strs[0][:i-1]
        return strs[0][:min_length]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    strs = ["aa","ab"]
    print(solution.longestCommonPrefix(strs))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
