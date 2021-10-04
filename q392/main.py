
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        if len(s)==0:
            return True
        if len(t)==0:
            return False
        while i<len(s):
            while j<len(t):
                if s[i]==t[j]:
                    i=i+1
                    j=j+1
                    break
                else:
                    j=j+1
            if j==len(t) and i<len(s):
                return False
            if i==len(s):
                return True





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "abc"
    t = "ahbgdc"
    # s = "axc"
    # t = "ahbgdc"
    # s=""
    # t="ahbgdc"
    # s="b"
    # t="abc"
    solution=Solution()
    print(solution.isSubsequence(s,t))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
