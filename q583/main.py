# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp=[[0]*(len(word2)+1) for i in range(1+len(word1))]
        for i in range(1,1+len(word1)):
            for j in range(1,1+len(word2)):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return len(word1)+len(word2)-2*dp[len(word1)][len(word2)]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    word1 = "leetcode"
    word2 = "etco"
    solution=Solution()
    print(solution.minDistance(word1,word2))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
