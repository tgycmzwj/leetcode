# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def areSentencesSimilar(self,sentence1:List[str],sentence2:List[str],similarPairs:List[List[str]])->bool:
        if len(sentence1)!=len(sentence2):return False
        dic={}
        for i in similarPairs:
            if i[0] not in dic:dic[i[0]]=[i[1]]
            else:dic[i[0]].append(i[1])
            if i[1] not in dic:dic[i[1]]=[i[0]]
            else:dic[i[1]].append(i[0])
        for i in range(len(sentence1)):
            if sentence1[i]!=sentence2[i]:
                if sentence1[i] not in dic or sentence2[i] not in dic:
                    return False
                if sentence1[i] not in dic[sentence2[i]]:
                    return False
        return True



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sentence1 = ["great","acting","skills"]
    sentence2 = ["fine","drama","talent"]
    similarPairs = [["great","fine"],["drama","acting"],["skills","talent"]]
    solution=Solution()
    print(solution.areSentencesSimilar(sentence1,sentence2,similarPairs))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
