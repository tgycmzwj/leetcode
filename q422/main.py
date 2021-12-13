# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        if max([len(i) for i in words])>len(words):
            return False
        for i in range(len(words)):
            words[i]=words[i]+' '*(len(words)-len(words[i]))
        for i in range(1,len(words)):
            for j in range(i):
                if words[i][j]!=words[j][i]:
                    return False
        return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    words = ["ball", "area", "read", "lady"]
    solution=Solution()
    print(solution.validWordSquare(words))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
