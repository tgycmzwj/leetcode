# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class WordDistance:
    def __init__(self, wordsDict: List[str]):
        self.wordsDict=wordsDict
        self.loc_dic={}
        for i in range(len(wordsDict)):
            if wordsDict[i] not in self.loc_dic.keys():
                self.loc_dic[wordsDict[i]]=[i]
            if wordsDict[i] in self.loc_dic.keys():
                self.loc_dic[wordsDict[i]].append(i)
    def shortest(self,w1,w2):
        pos1,pos2=self.loc_dic[w1],self.loc_dic[w2]
        min_dist=min([abs(i-j) for i in pos1 for j in pos2])
        return min_dist



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmds=["WordDistance", "shortest", "shortest"]
    vals=[[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]
    wordic=vals[0][0]
    obj=WordDistance(wordic)
    results=[None]
    for i in vals[1:]:
        results.append(obj.shortest(i[0],i[1]))
    print(results)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
