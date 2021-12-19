# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import Optional
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def split(self,s:str)->List[str]:
        try:
            first_left_par=s.index('(')
        except:
            return [s,None,None]
        balance=1
        i=0
        for i in range(first_left_par+1,len(s)):
            if s[i]=='(':balance=balance+1
            elif s[i]==')':balance=balance-1
            if balance==0:
                break
        if first_left_par+1>=i:
            left=None
        else:
            left=s[first_left_par+1:i]
        if i+2>=len(s)-1:
            right=None
        else:
            right=s[i+2:len(s)-1]
        return [s[:first_left_par],left,right]

    def str2tree(self, s: str) -> Optional[TreeNode]:
        if len(s)==0:
            return None
        threeparts=self.split(s)
        root=TreeNode(int(threeparts[0]))
        if not threeparts[1] or threeparts[1].isdigit():
            root.left=threeparts[1]
        else:
            root.left=self.str2tree(threeparts[1])
        if not threeparts[2] or threeparts[2].isdigit():
            root.right=threeparts[2]
        else:
            root.right=self.str2tree(threeparts[2])
        return root



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "4"
    solution=Solution()
    print(solution.str2tree(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
