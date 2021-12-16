# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from functools import lru_cache


class Solution:
    # @lru_cache(None)
    # def dp(self,i, j):
    #     if i == j:
    #         return 1
    #     elif i > j:
    #         return 0
    #     if s[i] == s[j]:
    #         return 2 + self.dp(i + 1, j - 1)
    #     else:
    #         return max(self.dp(i + 1, j), self.dp(i, j - 1))
    def dp(self,i, j):
        if self.dp_results[i][j]!=0:
            return self.dp_results[i][j]
        if i == j:
            self.dp_results[i][j]=1
            return 1
        elif i > j:
            self.dp_results[i][j] = 0
            return 0
        if s[i] == s[j]:
            self.dp_results[i][j] = 2 + self.dp(i+1,j-1)
            return self.dp_results[i][j]
        else:
            self.dp_results[i][j] = max(self.dp(i+1,j), self.dp(i,j-1))
            return self.dp_results[i][j]
    def longestPalindromeSubseq(self, s: str) -> int:
        self.dp_results=[[0]*len(s) for i in range(len(s))]
        return self.dp(0,len(s)-1)






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "bbbab"
    s="cjhdsjhagdsjhgasjghajsdghsjfhuiwehslhvbbd"
    solution=Solution()
    print(solution.longestPalindromeSubseq(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
