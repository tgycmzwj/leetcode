# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
import collections
class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1)!=len(sentence2):
            return False
        dic=collections.defaultdict(list)
        for w1,w2 in similarPairs:
            dic[w1].append(w2)
            dic[w2].append(w1)
        for w1,w2 in zip(sentence1,sentence2):
            if w1!=w2:
                flag=0
                processing=[w1]
                processed=[]
                while len(processing)>0:
                    cur_ele=processing.pop(0)
                    if cur_ele==w2:
                        flag=1
                        break
                    for an in dic[cur_ele]:
                        if an not in processed:
                            processing.append(an)
                            processed.append(an)
                if flag==0:return False
        return True

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sentence1 = ["I","love","leetcode"]
    sentence2 = ["I","love","onepiece"]
    similarPairs = [["manga","onepiece"],["platform","anime"],["leetcode","platform"],["anime","manga"]]
    solution=Solution()
    print(solution.areSentencesSimilarTwo(sentence1,sentence2,similarPairs))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
