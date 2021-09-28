# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict1={}
        dict2={}
        s=s.split(' ')
        if len(s)!=len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in dict1.keys() and s[i] not in dict2.keys():
                dict1[pattern[i]]=s[i]
                dict2[s[i]]=pattern[i]
            else:
                if pattern[i] in dict1.keys():
                    if dict1[pattern[i]]!=s[i]:
                        return False
                if s[i] in dict2.keys():
                    if dict2[s[i]]!=pattern[i]:
                        return False
        return True

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pattern = "abba"
    s = "dog cat cat dog"
    # pattern = "abba"
    # s = "dog cat cat fish"
    # pattern = "aaaa"
    # s = "dog cat cat dog"
    # pattern = "abba"
    # s = "dog dog dog dog"
    solution=Solution()
    print(solution.wordPattern(pattern,s))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
