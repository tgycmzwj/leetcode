# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def dis(self,pt1,pt2):
        return (pt1[0]-pt2[0])**2+(pt1[1]-pt2[1])**2
    def validSquare(self, p1, p2, p3, p4):
        if p1==p2==p3==p4:return False
        ls=[self.dis(p1,p2),self.dis(p1,p3),self.dis(p1,p4),self.dis(p2,p3),self.dis(p2,p4),self.dis(p3,p4)]
        ls.sort()
        if ls[0]==ls[1]==ls[2]==ls[3]:
            if ls[4]==ls[5]:
                return True
        return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    p1 = [0,0]
    p2 = [1,1]
    p3 = [1,0]
    p4 = [0,1]

    solution=Solution()
    print(solution.validSquare(p1,p2,p3,p4))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
