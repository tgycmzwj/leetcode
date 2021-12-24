# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def one_diff(self,str1,str2):
        for i in range(len(str1)):
            if str1[:i]==str2[:i] and str1[i+1:]==str2[i+1:]:
                return True
        return False
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if start==end:return 0
        if len(bank)==0:return -1
        processing=[[start]]
        processed=[]
        level=0
        while len(processing)!=0:
            cur_level=processing.pop(0)
            new_level=[]
            for cur_ele in cur_level:
                if cur_ele==end:return level
                processed.append(cur_ele)
                for bank_ele in bank:
                    if bank_ele not in processed and self.one_diff(cur_ele,bank_ele):
                        new_level.append(bank_ele)
            if len(new_level)>0:
                processing.append(new_level.copy())
            level=level+1
        return -1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start = "AACCTTGG"
    end="AATTCCGG"
    bank=["AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"]
    solution=Solution()
    print(solution.minMutation(start,end,bank))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
