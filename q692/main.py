# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic={}
        for i in words:
            if i not in dic:dic[i]=1
            else:dic[i]=dic[i]+1
        freq=[]
        for key,v in dic.items():
            freq.append(v)
        freq=sorted(freq,reverse=True)
        freq=freq[:k]
        results=[]
        for key,v in dic.items():
            if v in freq:
                results.append(key)
        results=sorted(results)
        return results[:k]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    words = ["i","love","leetcode","i","love","coding"]
    k = 2
    solution=Solution()
    print(solution.topKFrequent(words,k))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
