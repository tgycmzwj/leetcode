# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows=['qwertyuiop','asdfghjkl','zxcvbnm']
        rows[1]=rows[1]+rows[1].upper()
        results=[]
        for i in range(len(words)):
            cur_used=-1
            flag=0
            for j in range(len(words[i])):
                if flag==1:
                    break
                for k in range(len(rows)):
                    if words[i][j] in rows[k]:
                        if cur_used==-1:
                            cur_used=k
                        elif cur_used!=k:
                            flag=1
            if flag==0:
                results.append(words[i])
        return results





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    words = ["Hello", "Alaska", "Dad", "Peace"]
    words = ["omk"]
    words = ["adsdf", "sfd"]
    solution=Solution()
    print(solution.findWords(words))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
