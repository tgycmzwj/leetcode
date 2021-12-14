# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        res_dic={}
        for i in range(len(strings)):
            if len(strings[i])==1:
                if 'hehe' not in res_dic.keys():
                    res_dic['hehe']=[strings[i]]
                else:
                    res_dic['hehe'].append(strings[i])
            else:
                diff_seq=[]
                for j in range(len(strings[i])-1):
                    diff_seq.append(((ord(strings[i][j+1])-ord(strings[i][j]))+26)%26)
                diff_seq='_'.join([str(k) for k in diff_seq])
                if diff_seq not in res_dic.keys():
                    res_dic[diff_seq]=[strings[i]]
                else:
                    res_dic[diff_seq].append(strings[i])
        return list(res_dic.values())




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
    solution=Solution()
    print(solution.groupStrings(strings))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
