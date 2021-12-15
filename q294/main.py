# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def canWin(self, currentState: str) -> bool:
        self.mem={}
        return self.helper(currentState)
    def helper(self,s):
        if s in self.mem:
            return self.mem[s]
        for i in range(len(s)-1):
            if s[i]=='+' and s[i+1]=='+' and not self.helper(s[:i]+'--'+s[i+2:]):
                self.mem[s]=True
                return True
        self.mem[s]=False
        return False



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    currentState = "+++++"
    solution=Solution()
    print(solution.canWin(currentState))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
