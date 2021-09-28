# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s,t=list(s),list(t)
        s.sort()
        t.sort()
        if s!=t:
            return False
        return True

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    s="rat"
    t="car"
    solution=Solution()
    print(solution.isAnagram(s,t))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
