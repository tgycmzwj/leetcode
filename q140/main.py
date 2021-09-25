# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp_break={}
        for i in range(len(s)):
            dp_break[i]=[]
            if s[:i+1] in wordDict:
                dp_break[i].append([s[:i+1]])
            for j in range(i):
                if s[j+1:i+1] in wordDict:
                    for partition in dp_break[j]:
                        new_partition=partition.copy()
                        new_partition.append(s[j+1:i+1])
                        dp_break[i].append(new_partition)
        return [' '.join(item) for item in dp_break[len(s)-1]]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "pineapplepenapple"
    wordDict = ["apple","pen","applepen","pine","pineapple"]
    solution=Solution()
    print(solution.wordBreak(s,wordDict))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
