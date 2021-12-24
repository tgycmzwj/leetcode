# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def gen(self,word):
        if len(word)==0:return []
        if len(word)==1:return [word,'1']
        else:
            results=[]
            old_first=self.gen(word[1:])
            old_last=self.gen(word[:-1])
            for item in old_first:
                if item[0].isalpha():
                    results.append('1'+item)
                    results.append(word[0]+item)
                else:
                    pos=0
                    item=item+'$'
                    for pos in range(len(item)):
                        if item[pos].isalpha():
                            break
                    results.append(word[0]+item[:-1])
                    results.append(str(int(item[:pos])+1)+item[pos:-1])
            for item in old_last:
                if item[-1].isalpha():
                    results.append(item+'1')
                    results.append(item+word[-1])
                else:
                    pos=len(item)
                    item='$'+item
                    for pos in range(len(item)-1,-1,-1):
                        if item[pos].isalpha():
                            break
                    results.append(item[1:]+word[-1])
                    results.append(item[1:pos+1]+str(int(item[pos+1:])+1))
        return list(set(results))
    def generateAbbreviations(self, word: str) -> List[str]:
        results=self.gen(word)
        return results

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    word = "word"
    solution=Solution()
    print(solution.generateAbbreviations(word))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
