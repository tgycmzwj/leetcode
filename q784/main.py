# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        loc=[]
        for i in range(len(s)):
            if s[i].isalpha():
                loc.append(i)
        results=[]
        s=list(s)
        for i in range(2**len(loc)):
            s_copy=s.copy()
            bin_num=str(bin(i))[2:].zfill(len(loc))
            for j in range(len(bin_num)):
                if bin_num[j]=='1':
                    if s[loc[j]].islower():
                        s_copy[loc[j]]=s_copy[loc[j]].upper()
                    else:
                        s_copy[loc[j]]=s_copy[loc[j]].lower()
            results.append(''.join(s_copy))
        return results


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "a1b2"
    solution=Solution()
    print(solution.letterCasePermutation(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
