# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        s='$'+s
        dp=[1]*len(s)
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                dp[i]=dp[i-1]+1
            else:
                j=i-1
                for j in range(i-1,-1,-1):
                    if s[j]!=s[i-1] and s[j]!=s[i]:
                        break
                dp[i]=i-j
        return max(dp)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "ccaabbb"
    s = "eceba"
    solution=Solution()
    print(solution.lengthOfLongestSubstringTwoDistinct(s))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
