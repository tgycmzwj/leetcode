# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        cur_max=0
        for i in range(len(words)):
            words[i]=list(words[i])
        for i in range(len(words)-1):
            for j in range(i,len(words)):
                if len(words[i])*len(words[j])>cur_max:
                    if len(set(words[i]))+len(set(words[j])) ==len(set(words[i]+words[j])):
                        cur_max=len(words[i])*len(words[j])
        return cur_max

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    words = ["abcw","baz","foo","bar","xtfn","abcdef"]
    solution=Solution()
    print(solution.maxProduct(words))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
