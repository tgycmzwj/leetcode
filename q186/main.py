# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i],s[len(s)-1-i]=s[len(s)-1-i],s[i]
        start,end=0,0
        for i in range(len(s)+1):
            if i==len(s) or s[i]==' ':
                end=i
                for j in range(0,(end-start)//2):
                    s[start+j],s[end-1-j]=s[end-1-j],s[start+j]
                start=end+1
        return s

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
    s=['a']
    solution=Solution()
    print(solution.reverseWords(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
