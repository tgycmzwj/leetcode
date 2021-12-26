# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic={}
        for i in range(len(order)):
            dic[order[i]]=i
        def sort_func(word):
            results=[]
            for i in word:results.append(dic[i])
            return results
        sorted_words=sorted(words,key=sort_func)
        return words==sorted_words

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    words = ["hello","leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    solution=Solution()
    print(solution.isAlienSorted(words,order))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
