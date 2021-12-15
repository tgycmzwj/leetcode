# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class ValidWordAbbr:
    def __init__(self, dictionary: List[str]):
        self.dic={}
        for i in dictionary:
            #find key
            if len(i)<=2:
                k=i
            else:
                k=i[0]+str(len(i)-2)+i[-1]
            #append
            if k not in self.dic.keys():
                self.dic[k]=[i]
            else:
                if i not in self.dic[k]:
                    self.dic[k].append(i)
    def isUnique(self, word: str) -> bool:
        if len(word) <= 2:
            k = word
        else:
            k = word[0] + str(len(word) - 2) + word[-1]
        if k not in self.dic.keys():
            return True
        elif self.dic[k][0]==word and len(self.dic[k])==1:
            return True
        return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmds=["ValidWordAbbr", "isUnique", "isUnique", "isUnique", "isUnique", "isUnique"]
    vals=[[["deer", "door", "cake", "card"]], ["dear"], ["cart"], ["cane"], ["make"], ["cake"]]
    results=[]
    for i in range(len(cmds)):
        cmd,val=cmds[i],vals[i][0]
        if cmd=='ValidWordAbbr':
            obj=ValidWordAbbr(val)
            results.append(None)
        else:
            results.append(obj.isUnique(val))
    print(results)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
