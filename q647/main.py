# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution(object):
    def countSubstrings(self, s):
        # dp[i][j]=1 if a substring starting from j, ending at i is palindrames
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        for i in range(len(s)):
            for j in range(i):
                if (i-j==1) and (s[i]==s[j]):
                    dp[i][j]=1
                elif (dp[i-1][j+1]==1) and (s[i]==s[j]):
                    dp[i][j]=1
        return sum([sum(i) for i in dp])



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "ababsdaf"
    solution=Solution()
    print(solution.countSubstrings(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
