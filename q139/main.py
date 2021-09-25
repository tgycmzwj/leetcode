# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp_break=[0]*len(s)
        for i in range(len(s)):
            if s[:i+1] in wordDict:
                dp_break[i]=1
                continue
            for j in range(i):
                if dp_break[j]==1 and s[j+1:i+1] in wordDict:
                    dp_break[i]=1
        return dp_break[-1]==1




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "catsandog"
    wordDict = ["cats","dog","sand","and","cat"]
    solution=Solution()
    print(solution.wordBreak(s,wordDict))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
