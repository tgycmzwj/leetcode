# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def diff_by1(self,s1,s2):
        #s1 is shorter
        if abs(len(s1)-len(s2))!=1:
            return False
        for i in range(0,len(s1)+1):
            if s1[:i]==s2[:i] and s1[i:]==s2[i+1:]:
                return True
        return False
    def longestStrChain(self, words: List[str]) -> int:
        words=list(set(words))
        words=sorted(words,key=lambda x: len(x))
        #length
        length={}
        for i in words:
            if len(i) in length.keys():
                length[len(i)].append(i)
            else:
                length[len(i)]=[i]
        #position
        pos={}
        for i in range(len(words)):
            pos[words[i]]=i
        #longest if this is the last word
        dp_longest_as_last=[1]*len(words)
        for i in range(len(dp_longest_as_last)):
            if len(words[i])-1 in length.keys():
                for cand in length[len(words[i])-1]:
                    if self.diff_by1(cand,words[i]):
                        dp_longest_as_last[i]=max(dp_longest_as_last[i],dp_longest_as_last[pos[cand]]+1)
        return max(dp_longest_as_last)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    words = ["a","b","ba","bca","bda","bdca"]
    #words=["xbc","pcxbcf","xb","cxbc","pcxbc"]
    words = ["abcd","dbqca"]
    solution=Solution()
    print(solution.longestStrChain(words))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
