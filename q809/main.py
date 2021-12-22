# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def compress(self,s:str):
        results=[]
        s=' '+s+' '
        counter=1
        for i in range(1,len(s)):
            if s[i]!=s[i-1]:
                results.append([s[i-1],counter])
                counter=1
            else:
                counter=counter+1
        return results[1:]
    def expressiveWords(self, s: str, words: List[str]) -> int:
        s=self.compress(s)
        counter=0
        for i in range(len(words)):
            word=self.compress(words[i])
            if len(word)!=len(s):continue
            flag=0
            for j in range(len(s)):
                if s[j][0]!=word[j][0] or s[j][1]<word[j][1]:
                    flag=1
                if word[j][1]==1 and s[j][1]==2:
                    flag=1
            if flag==0:
                counter=counter+1
        return counter

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "zzzzzyyyyy"
    words = ["zzyy","zy","zyy"]
    solution=Solution()
    print(solution.expressiveWords(s,words))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
