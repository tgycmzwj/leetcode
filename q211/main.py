# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import re
class WordDictionary:

    def __init__(self):
        self.list=[]

    def addWord(self, word: str) -> None:
        if word not in self.list:
            self.list.append(word)
    def search(self, word: str) -> bool:
        for i in self.list:
            if len(word)!=len(i):
                continue
            if re.search(word,i) and len(word)==len(i):
                return True
        return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmds_content=["WordDictionary","addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"]
    cmds_value=[[],["at"],["and"],["an"],["add"],["a"],[".at"],["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]]
    results=[]
    for i in range(len(cmds_content)):
        cmd_content=cmds_content[i]
        cmd_value=cmds_value[i]
        if cmd_content=='WordDictionary':
            obj=WordDictionary()
            results.append(None)
        elif cmd_content=='addWord':
            results.append(obj.addWord(cmd_value[0]))
        elif cmd_content=='search':
            results.append(obj.search(cmd_value[0]))
    print(results)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
