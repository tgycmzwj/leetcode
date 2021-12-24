# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp=[0]*len(s) #ending at i
        for i in range(1,len(s)):
            if s[i]==')':
                #()
                if s[i-1]=='(':
                    dp[i]=dp[i-2]+2
                #((())
                elif i-dp[i-1]-1>=0 and s[i-dp[i-1]-1]=='(':
                    if dp[i-1]>0:
                        dp[i]=dp[i-1]+2+dp[i-dp[i-1]-2]
                    else:
                        dp[i]=0
        return max(dp)


            


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = ")()())"
    solution=Solution()
    print(solution.longestValidParentheses(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
