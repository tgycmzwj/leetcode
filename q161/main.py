# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s==t:return False
        if abs(len(s)-len(t))>1: return False
        if len(s)==len(t):
            for i in range(len(s)-1):
                if s[:i]==t[:i] and s[i+1:]==t[i+1:]:
                    return True
            if len(t)==0 or len(t)==1:
                return True
            return False
        if len(s)<len(t):
            s,t=t,s
        if len(s)>len(t):
            for i in range(len(t)+1):
                if s[:i]==t[:i] and s[i+1:]==t[i:]:
                    return True
            if len(t)==0:
                return True
            return False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "a"
    t = "ac"
    solution=Solution()
    print(solution.isOneEditDistance(s,t))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
