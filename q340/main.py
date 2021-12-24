# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k==0:return 0
        s = '$' + s
        dp = [[1,{}] for i in range(len(s))]  #set change to {}, keep track both char and location
        for i in range(0, len(s)):
            if i==0:
                dp[i][1][s[i]]=0
                continue
            if s[i] in dp[i-1][1]:
                dp[i][0]=dp[i-1][0]+1
                dp[i][1]=dp[i-1][1].copy()
                dp[i][1][s[i]]=i
            else:
                earliest_location=min(dp[i-1][1].values())
                dp[i][0]=i-earliest_location+1
                dp[i][1]=dp[i-1][1].copy()
                dp[i][1][s[i]]=i
                if len(dp[i][1])>k:
                    for key,v in dp[i][1].items():
                        if v==earliest_location:
                            del dp[i][1][key]
                            break
        return max([item[0] for item in dp])-1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "dsjhfaskfhaskfhsakdfhsjafhjsafhassadjfhsafsadfdsaghjskfhjskfhsjfshdfjsahfasjdhf"
    k = 4
    solution=Solution()
    print(solution.lengthOfLongestSubstringKDistinct(s,k))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
