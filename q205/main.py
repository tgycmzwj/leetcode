# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_dic1={}
        mapping_dic2={}
        for i in range(len(s)):
            if s[i] not in mapping_dic1.keys() and t[i] not in mapping_dic2.keys():
                mapping_dic1[s[i]]=t[i]
                mapping_dic2[t[i]]=s[i]
            else:
                if s[i] in mapping_dic1.keys():
                    if mapping_dic1[s[i]]!=t[i]:
                        return False
                if t[i] in mapping_dic2.keys():
                    if mapping_dic2[t[i]]!=s[i]:
                        return False
        return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    s = "egg"
    t = "add"
    # s = "foo"
    # t = "bar"
    # s = "paper"
    # t = "title"
    # s="badc"
    # t="baba"
    print(solution.isIsomorphic(s,t))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
