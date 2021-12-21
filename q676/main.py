# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class MagicDictionary:
    def __init__(self):
        self.dic=set()
    def buildDict(self, dictionary: List[str]) -> None:
        for item in dictionary:
            for i in range(len(item)):
                for var in 'abcdefghijklmnopqrstuvwxyz':
                    if item[i]!=var:
                        self.dic.add(item[:i]+var+item[i+1:])
    def search(self, searchWord: str) -> bool:
        return searchWord in self.dic

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmds=["MagicDictionary", "buildDict", "search", "search", "search", "search"]
    vals=[[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
