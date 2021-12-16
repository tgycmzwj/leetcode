# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def sub(self,x,y):   #whether x is a substring of y
        if len(x)>len(y):
            return False
        if len(x)==len(y) and x!=y:
            return False
        pos=0
        for i in y:
            if i==x[pos]:
                pos=pos+1
                if pos==len(x):
                    return True
        return False
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary=sorted(dictionary,key=lambda x:(-len(x),x))
        if len(s)<len(dictionary[-1]):
            return ''
        for i in range(len(dictionary)):
            if self.sub(dictionary[i],s):
                return dictionary[i]
        return ''

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "abpcplea"
    dictionary = ["ale","apple","monkey","plea"]
    solution=Solution()
    print(solution.findLongestWord(s,dictionary))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
