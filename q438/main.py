# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
import collections
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        myDictP=collections.Counter(p)
        myDictS=collections.Counter(s[:len(p)])
        output=[]
        i=0  #start point
        j=len(p)   #end point
        while j<=len(s):
            if myDictS==myDictP:
                output.append(i)
            myDictS[s[i]]-=1
            if myDictS[s[i]]<=0:
                myDictS.pop(s[i])
            if j<len(s):
                 myDictS[s[j]]+=1
            j+=1
            i+=1
        return output

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    solution=Solution()
    print(solution.findAnagrams(s,p))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
