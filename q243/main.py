# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        pos1,pos2=-1e5,1e5
        min_dist=1e5
        for i in range(len(wordsDict)):
            if word1==wordsDict[i]:
                pos1=i
            if word2==wordsDict[i]:
                pos2=i
            min_dist=min(min_dist,abs(pos1-pos2))
        return min_dist

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
    word1 = "makes"
    word2 = "coding"
    solution=Solution()
    print(solution.shortestDistance(wordsDict,word1,word2))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
