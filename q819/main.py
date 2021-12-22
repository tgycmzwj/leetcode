# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        dic={}
        for sym in "!?',;.":
            paragraph=paragraph.replace(sym,' ')
        while '  ' in paragraph:
            paragraph=paragraph.replace('  ',' ')
        max_counter=1
        for i in paragraph.split(' '):
            if i.lower() not in banned:
                if i.lower() not in dic:dic[i.lower()]=1
                else:
                    dic[i.lower()]=dic[i.lower()]+1
                    max_counter=max(max_counter,dic[i.lower()])
        for k,v in dic.items():
            if v==max_counter:
                return k

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    solution=Solution()
    print(solution.mostCommonWord(paragraph,banned))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
